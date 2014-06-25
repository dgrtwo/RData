library("ggplot2")
library(data.table)
 if (!exists("pitching")) { pitching = as.data.table(read.csv("http://dgrtwo.github.io/pages/lahman/Pitching.csv")) } else { pitching = as.data.table(pitching) }