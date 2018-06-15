args = commandArgs(trailingOnly = TRUE)

if(length(args) != 2){
  stop("Input arguments should be 2")
}else{
  input_file = args[1]
  output_file = args[2]
  print(paste("Converting GT3X raw csv file"))
  df = MIMSunit::import_actigraph_raw(input_file, ts_provided=FALSE, header_provided=TRUE)
  print(paste("Saving converted GT3X file"))
  write.csv(x = df, file = output_file, append = FALSE, quote = FALSE, row.names = FALSE)
  print(paste("Completed"))
}