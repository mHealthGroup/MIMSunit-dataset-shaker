args = commandArgs(trailingOnly = TRUE)

if(length(args) != 2){
  stop("Input arguments should be 2")
}else{
  input_file = args[1]
  output_file = args[2]
  print(paste("Converting Actigraph raw csv file"))
  df = MIMSunit::import_actigraph_raw(input_file, ts_provided=TRUE, header_provided=TRUE)
  print(paste("Saving converted Actigraph file"))
  dir.create(dirname(output_file), showWarnings=FALSE, recursive=TRUE)
  write.csv(x = df, file = output_file, append = FALSE, quote = FALSE, row.names = FALSE)
  print(paste("Completed"))
}