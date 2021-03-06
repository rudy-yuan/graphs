#!/usr/bin/env Rscript

suppressPackageStartupMessages (library(ggplot2))
suppressPackageStartupMessages (library(reshape2))
## suppressPackageStartupMessages (library(doBy))

source ("face-flow-style.R")


MDPF3.data = read.table ('/home/rudy/ns-dev/experimentResult/results/congestion-zoom-ndn-MDPF3-100-rate-trace.log', header = TRUE, sep = "\t")
MDPF3.data$Node = factor (MDPF3.data$Node)
MDPF3.data$Type = factor (MDPF3.data$Type)
MDPF3.data = subset (MDPF3.data, Type == "InData" & Node == "clientProvider" & FaceId != "0")[,c(1,2,3,7)]

# this is used to draw ndn with entropy routing
EPF2.data = read.table ('/home/rudy/ns-dev/experimentResult/results/congestion-zoom-ndn-EPF3-100-rate-trace.log', header = TRUE, sep = "\t")
EPF2.data$Node = factor (EPF2.data$Node)
EPF2.data$Type = factor (EPF2.data$Type)
EPF2.data = subset (EPF2.data, Type == "InData" & Node == "clientProvider" & FaceId != "0")[,c(1,2,3,7)]


BestRoute.data = read.table ('/home/rudy/ns-dev/experimentResult/results/congestion-zoom-ndn-BestRoute-100-rate-trace.log', header = TRUE, sep = "\t")
BestRoute.data$Node = factor (BestRoute.data$Node)
BestRoute.data$Type = factor (BestRoute.data$Type)
BestRoute.data = subset (BestRoute.data, Type == "InData" & Node == "clientProvider" & FaceId != "0")[,c(1,2,3,7)]

names (BestRoute.data) = names (EPF2.data)


MDPF3.data$Type = "MDPF3"
BestRoute.data$Type = "BestRoute"
EPF2.data$Type = "EPF"


data = rbind (BestRoute.data,MDPF3.data,EPF2.data)


g <- ggplot (data=data ,aes(x=Time, y=Kilobytes,color = factor(FaceId),shape = factor(FaceId)) ) +
  geom_point(size=1.65) +

  ylab ("链路使用率 [Kilobytes/s]") +
  xlab ("时间 [秒]")+
  scale_x_continuous(limits=c(0, 70),breaks=seq(0,70,10))+
  facet_wrap (~ Type) +
  stat_smooth(se = FALSE)+

  scale_shape_discrete(name="Link")+
  

  scale_color_manual (name="Link", values = c('blue2', 'red4','darkgreen')) +

  theme_custom () + theme(legend.position=c(0.9,0.8)) + theme(legend.key.height=unit(0.9,'cm'))





cat ("Writing graph to [face-flow-pf.pdf]\n")
pdf (file = "./graphs/face-flow-pf.pdf",width=9,height=6)
# g+theme(legend.position=c(0.9,0.8))
g
x = dev.off ();

