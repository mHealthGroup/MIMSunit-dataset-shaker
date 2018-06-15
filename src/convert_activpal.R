args = commandArgs(trailingOnly = TRUE)

if(length(args) != 2){
  stop("Input arguments should be 2")
}else{
  input_file = args[1]
  output_file = args[2]
  print(paste("Converting activpal raw csv file"))
  df = MIMSunit::import_activpal_raw(input_file, header_provided=FALSE)
  print(paste("Saving converted activpal file"))
  write.csv(x = df, file = output_file, append = FALSE, quote = FALSE, row.names = FALSE)
  print(paste("Completed"))
}