library("ggplot2")
library(data.table)
 if (!exists("pitching")) { pitching = as.data.table(read.csv("http://dgrtwo.github.io/pages/lahman/Pitching.csv")) } else { pitching = as.data.table(pitching) }
 if (!exists("salaries")) { salaries = as.data.table(read.csv("http://dgrtwo.github.io/pages/lahman/Salaries.csv")) } else { salaries = as.data.table(salaries) }
 merged = merge(pitching, salaries, by=c("lgID", "playerID", "teamID", "yearID"))