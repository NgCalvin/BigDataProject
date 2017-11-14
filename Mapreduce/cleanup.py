#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

SCORE_MIN = 1
SCORE_MAX = 5


def cleanup(reduced_result, top_max):
    #get mapped result
    data = reduced_result

    # sort by score asc, k-length asc, frequency desc, alphabetic asc
    sorter = [(0,False),(1,False),(2,True),(3,False)]

    #sort data
    for (key, rev) in reversed(sorter):
    	data = sorted(data, key = itemgetter(key), reverse=rev)

    prev_score = SCORE_MIN-1
    prev_k = 1-1
    count = 0
    
    for line in data:
    	#current score and k-length for this record
    	score = line[0]
    	k = line[1]

    	#if it is beginning of new group i.e. different k-length / score with previous
    	if (k != prev_k) | (score != prev_score):
    		count = 0
    		print "top {} for score = {} and k-length = {}".format(top_max,score,k)

    	#if already outputted top n frequent words in the same group, skip
    	if count == top_max:
    		continue

        #output score, k-length, frequency, k-shingle
        print "score: {}, k-length: {}, frequency: {}, shingle: {}".format(line[0],line[1],line[2],line[3])
        
        count += 1
        prev_score = score
    	prev_k = k