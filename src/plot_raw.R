
library(ggplot2)
args = commandArgs(trailingOnly = TRUE)

if(length(args) < 2){
  stop("Input arguments should be greater than 1")
}else{
  input_file = args[1]
  output_file = args[2]
  df = mHealthR::mhealth.read(input_file, filetype='sensor')
  p = mHealthR::mhealth.plot_timeseries(dfs=list(df), file_types=c('sensor'), select_cols=list(c(2,3,4)), group_cols=c('HZ'))
  ggsave(filename=output_file, plot=p)
}