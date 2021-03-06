#!/usr/bin/env Rscript

suppressPackageStartupMessages (library(ggplot2))
suppressPackageStartupMessages (library(reshape2))
## suppressPackageStartupMessages (library(doBy))

source ("averageFlow-style.R")

entropyRouting.data = read.table ('../averageDropRate-100.txt', header = TRUE, sep = "\t")
entropyRouting.data$Type = factor (entropyRouting.data$Type)

g <- ggplot (data=entropyRouting.data, aes(x=Time, y=AverageDrop, group =Type , shape = Type,color = Type,linetype = Type)) +

  geom_point(size=2)+
  geom_line(size=0.2)+
  scale_color_manual (values = c('blue2', 'red4', 'darkgreen','black')) +

  scale_x_continuous(limits=c(0, 50),breaks=seq(0,50,10))+
  xlab ("Time [second]") +
  ylab ("Drop Rate [Kilobytes/s]") +

  theme_custom ()


cat ("Writing graph to [DropData.pdf]\n")
pdf (file = "extend-DropData.pdf",width=9,height=6)
g
x = dev.off ();