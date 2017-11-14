#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

SCORE_MIN = 1
SCORE_MAX = 5


def cleanup(reduced_result, k_max, top_max, separator='\t'):
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
    	score = line[0]
    	k = line[1]

    	if k != prev_k:
    		count = 0
    		print "top {} for score = {} and k-length = {}".format(top_max,score,k)

    	if count == top_max:
    		continue

        #output score, k-length, frequency, k-shingle
        print "score: {}, k-length: {}, frequency: {}, shingle: {}".format(line[0],line[1],line[2],line[3])
        
        count += 1
        prev_score = score
    	prev_k = k