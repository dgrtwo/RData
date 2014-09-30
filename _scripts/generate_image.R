#!/usr/bin/Rscript --vanilla
# create the image used as the icon for the Coursera course

library(ggplot2)
data(diamonds)

g <- ggplot(diamonds, aes(carat, price, color=color)) + geom_point(aes(shape=cut)) +
    stat_smooth() + xlab("") + ylab("")

ggsave("public/icon.png", g, width=600/72, height=340/72)
