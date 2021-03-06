#!/usr/bin/env python
# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-
import string 


f_out = open ("/home/rudy/ns-dev/experimentResult/graphs/r/face_result.txt" , "w")

f_out.write ("Type\tFace0\tFace1\tFace2\tFace3\n")

runs = range(15,16)
for run in runs:
    face_0 = 0
    face_1 = 0
    face_2 = 0
    face_3 = 0
    f_in = open ("/home/rudy/ns-dev/experimentResult/graphs/deviation_face.log", "r")

    for line in f_in:
        #f_out.write ("%s" % line)
        a = line.split('\t')
        face = string.atoi(a[0])
        if face == 0:
	  face_0 += 1
        if face == 1:
	  face_1 += 1
	if face == 2:
	  face_2 += 1
	if face == 3:
	  face_3 += 1
	    
    f_out.write("deviationRouting\t%d\t%d\t%d\t%d\n"%(face_0,face_1,face_2,face_3)) 
    print "deviationRouting\t%d\t%d\t%d\n"%(face_1,face_2,face_3)
    
    face_0 = 0
    face_1 = 0
    face_2 = 0
    face_3 = 0
    f_in = open ("/home/rudy/ns-dev/experimentResult/graphs/deviation2_face.log", "r")

    for line in f_in:
        #f_out.write ("%s" % line)
        a = line.split('\t')
        face = string.atoi(a[0])
        if face == 0:
	  face_0 += 1
        if face == 1:
	  face_1 += 1
	if face == 2:
	  face_2 += 1
	if face == 3:
	  face_3 += 1
	    
    f_out.write("deviationRouting2\t%d\t%d\t%d\t%d\n"%(face_0,face_1,face_2,face_3))  
    print "deviationRouting2\t%d\t%d\t%d\n"%(face_1,face_2,face_3)
     
    face_0 = 0
    face_1 = 0
    face_2 = 0
    face_3 = 0
    f_in = open ("/home/rudy/ns-dev/experimentResult/graphs/best_face.log", "r")

    for line in f_in:
        #f_out.write ("%s" % line)
        a = line.split('\t')
        face = string.atoi(a[0])
        if face == 0:
	  face_0 += 1
        if face == 1:
	  face_1 += 1
	if face == 2:
	  face_2 += 1
	if face == 3:
	  face_3 += 1
	    
    f_out.write("bestRouting\t%d\t%d\t%d\t%d\n"%(face_0,face_1,face_2,face_3))  
    print "bestRouting\t%d\t%d\t%d\n"%(face_1,face_2,face_3)
    

    face_0 = 0
    face_1 = 0
    face_2 = 0
    face_3 = 0
    f_in = open ("/home/rudy/ns-dev/experimentResult/graphs/optimal_face.log", "r")

    for line in f_in:
        #f_out.write ("%s" % line)
        a = line.split('\t')
        face = string.atoi(a[0])
        if face == 0:
	  face_0 += 1
        if face == 1:
	  face_1 += 1
	if face == 2:
	  face_2 += 1
	if face == 3:
	  face_3 += 1
	    
    f_out.write("optimalRouting\t%d\t%d\t%d\t%d\n"%(face_0,face_1,face_2,face_3))  
    print "optimalRouting\t%d\t%d\t%d\n"%(face_1,face_2,face_3)