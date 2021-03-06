#!/usr/bin/env Rscript

suppressPackageStartupMessages (library(ggplot2))
suppressPackageStartupMessages (library(reshape2))
## suppressPackageStartupMessages (library(doBy))

source ("averageDropRate-style.R")

entropyRouting.data = read.table ('hitRatio.txt', header = TRUE, sep = "\t")
entropyRouting.data$Type = factor (entropyRouting.data$Type)

g <- ggplot (data=entropyRouting.data, aes(x=Time, y=Ratio, group =Type , shape = Type,color = Type,linetype = Type)) +

  geom_point(size=0.5)+
  geom_line(size=0.5)+
  scale_color_manual (values = c('blue2', 'red4', 'darkgreen')) +
  scale_x_continuous(limits=c(0, 50),breaks=seq(0,50,10))+
  xlab ("Time [second]") +
  ylab ("Cache Hit Ratio [%]") +

  theme_custom () + theme(legend.position=c(0.8,0.2)) + theme(legend.key.height=unit(0.9,'cm'))


cat ("Writing graph to [ratioZipf1500.pdf]\n")
pdf (file = "ratioZipf1500.pdf",width=9,height=6)
g
x = dev.off ();