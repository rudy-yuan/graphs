#!/usr/bin/env python
# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-
import string 


f_out = open ("delay.txt" , "w")
f_out.write ("Type\tSeqNo\tDelay\n")

types = ["BestRoute","MDBF3", "EBF3"]
for t in types:

    f_in = open ("/home/rudy/ns-dev/experimentResult/results/congestion-zoom-ndn-%s-100-app-delays-trace.log" % t , "r")
    for line in f_in:
        a=line.split('\t')
        if a[1]=='client' and a[4]=='FullDelay':
            delay = string.atof(a[5])*1000
            if delay > 2000.0:
                f_out.write("%s\t%d\t%f\n" % (t, string.atoi(a[3]), 2000.0))
            else:
                f_out.write("%s\t%d\t%f\n" % (t, string.atoi(a[3]), delay))

f_out.close