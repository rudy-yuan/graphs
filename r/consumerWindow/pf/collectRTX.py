#!/usr/bin/env python
# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-
import string 

f = open("textRatio.txt", "w")
f.write("Type Ratio\n")

f_out = open ("retx.txt" , "w")
f_out.write ("Type\tSeqNo\tRetxCount\n")

types = ["BestRoute","MDPF3", "EPF3"]
for t in types:

    total = 0
    RetxCount = 0
    f_in = open ("/home/rudy/ns-dev/experimentResult/results/congestion-zoom-ndn-%s-100-app-delays-trace.log" % t , "r")
    for line in f_in:
        a=line.split('\t')
        if a[1]=='client' and a[4]=='FullDelay':
            count = string.atoi(a[7])
            total += count
            f_out.write("%s\t%d\t%d\n" % (t, string.atoi(a[3]), count))
            if count > 1:
                RetxCount += count-1      
    f.write("%s %f\n" % (t, RetxCount/(total+0.0)))