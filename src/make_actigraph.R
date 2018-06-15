args = commandArgs(trailingOnly = TRUE)

if(length(args) != 2){
  stop("Input arguments should be 2")
}else{
  input_file = args[1]
  output_file = args[2]
  print(paste("Make Actigraph raw csv file from mhealth file"))
  df = mHealthR::mhealth.read(input_file, filetype = 'sensor')
  dir.create(dirname(output_file), showWarnings=FALSE, recursive=TRUE)
  MIMSunit::export_actigraph_raw(df, output_file)
  print(paste("Completed"))
}