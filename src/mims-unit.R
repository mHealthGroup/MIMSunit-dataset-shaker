args = commandArgs(trailingOnly = TRUE)

if(length(args) < 2){
  stop("Input arguments should be greater than 2")
}else{
  input_file = args[1]
  before_file = args[2]
  after_file = args[3]
  output_file = args[4]
  grange = as.numeric(args[5])

  low_cutoff = args[6]
  if(low_cutoff == 'NULL'){
    low_cutoff = 0.2
  }else{
    low_cutoff = as.numeric(args[6])
  }
  
  high_cutoff = args[7]
  if(high_cutoff == 'NULL'){
    high_cutoff = 5
  }else{
    high_cutoff = as.numeric(args[7])
  }

  cutoffs = c(low_cutoff, high_cutoff)

  use_extrapolation = args[8]
  
  if(use_extrapolation == 'True'){
    use_extrapolation = TRUE
  }else{
    use_extrapolation = FALSE
  }

  print(grange)
  if(before_file == 'NULL'){
    before_file = NULL
  }
  if(after_file == 'NULL'){
    after_file = NULL
  }
  print(paste("Input file is:", input_file))
  print(paste("Before file is:", before_file))
  print(paste("After file is:", after_file))
  print(paste("Output file is:", output_file))
  print(paste("Loading file..."))
  dat = mHealthR::mhealth.read(file = input_file, filetype = "sensor")
  if(!is.null(before_file)){
    print("Get the last 2 minutes data for before file")
    before_dat = mHealthR::mhealth.read(file = before_file, filetype = "sensor")
    before_dat = mHealthR::mhealth.clip(before_dat, start_time = dat[1,1] - 120, stop_time = dat[1,1], file_type = "sensor")
  }else{
    before_dat = NULL
  }
  if(!is.null(after_file)){
    print("Get the first 2 minutes data for after file")
    after_dat = mHealthR::mhealth.read(file = after_file, filetype = "sensor")
    after_dat = mHealthR::mhealth.clip(after_dat, start_time = dat[nrow(dat),1], stop_time = dat[nrow(dat),1] + 120, file_type = "sensor")
  }else{
    after_dat = NULL
  }

  print(paste("Computing MIMS-unit..."))
  output_dat = MIMSunit::mims_unit(df = dat, breaks = "5 sec", range = c(-grange, grange), before_df = before_dat, after_df = after_dat, cutoffs = cutoffs, use_extrapolation = use_extrapolation)
  print(paste("Saving MIMS-unit..."))
  write.csv(x = output_dat, file = output_file, append = FALSE, quote = FALSE, row.names = FALSE)
  print(paste("Completed"))
}