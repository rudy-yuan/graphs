#!/usr/bin/env python
# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-
import string 


f_out = open ("3averageETR.txt" , "w")

f_out.write ("Type\tFrequency\tAverageETR\n")

runs = range(1,47)
for run in runs:

    f_in = open ("/home/rudy/ns-dev/experimentResult/results/congestion-zoom-ndn-bestRouting-%d-app-delays-trace.log" % run , "r")
    retx_count=0
    all_count=0
    for line in f_in:
        a=line.split('\t')
        if a[1]=='client' and a[4]=='FullDelay':
	    retx_count += string.atoi(a[7])-1
            all_count += string.atoi(a[7])
    
    print "Type= bestRouting:"
    print "retx count=%d " % retx_count
    print "all count=%d\n" % all_count
    print "ETR=%f\n" % ((all_count-retx_count)/(all_count+0.0))
    f_out.write("BestRoute\t%d\t%f\n" % (run*100, ((all_count-retx_count)/(all_count+0.0))))
    
    f_in = open ("/home/rudy/ns-dev/experimentResult/results/congestion-zoom-ndn-optimalRouting-%d-app-delays-trace.log" % run , "r")
    retx_count=0
    all_count=0
    for line in f_in:
        a=line.split('\t')
        if a[1]=='client' and a[4]=='FullDelay':
	    retx_count += string.atoi(a[7])-1
            all_count += string.atoi(a[7])
    
    print "Type= optimalRouting:"
    print "retx count=%d " % retx_count
    print "all count=%d\n" % all_count
    print "ETR=%f\n" % ((all_count-retx_count)/(all_count+0.0))
    f_out.write("OptimalRoute\t%d\t%f\n" % (run*100, ((all_count-retx_count)/(all_count+0.0))))
    
    f_in = open ("/home/rudy/ns-dev/experimentResult/results/congestion-zoom-ndn-deviationRouting-%d-app-delays-trace.log" % run , "r")
    retx_count=0
    all_count=0
    for line in f_in:
        a=line.split('\t')
        if a[1]=='client' and a[4]=='FullDelay':
	    retx_count += string.atoi(a[7])-1
            all_count += string.atoi(a[7])
    
    print "Type= deviationRouting:"
    print "retx count=%d " % retx_count
    print "all count=%d\n" % all_count
    print "ETR=%f\n" % ((all_count-retx_count)/(all_count+0.0))
    f_out.write("DeviationRoute\t%d\t%f\n" % (run*100, ((all_count-retx_count)/(all_count+0.0))))
    
    f_in = open ("/home/rudy/ns-dev/experimentResult/results/congestion-zoom-ndn-deviationRouting3-%d-app-delays-trace.log" % run , "r")
    retx_count=0
    all_count=0
    for line in f_in:
        a=line.split('\t')
        if a[1]=='client' and a[4]=='FullDelay':
	    retx_count += string.atoi(a[7])-1
            all_count += string.atoi(a[7])
    
    print "Type= deviationRouting3:"
    print "retx count=%d " % retx_count
    print "all count=%d\n" % all_count
    print "ETR=%f\n" % ((all_count-retx_count)/(all_count+0.0))
    f_out.write("DeviationRoute3\t%d\t%f\n" % (run*100, ((all_count-retx_count)/(all_count+0.0))))
   
f_out.close