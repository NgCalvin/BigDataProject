#!/usr/bin/env python


import sys

import csv
from itertools import groupby
from operator import itemgetter


SCORE_MIN = 1
SCORE_MAX = 5


def filter_result(file_name, top_max):
    #get mapped result
    data = list(csv.reader(open(file_name, 'rb'), delimiter='\t'))
    #data format: score, k-length, k-shingle, count
    #change to: score, k-length, count, k-shingle
    #make count to be integer for sorting
    for line in data:
        line[2] , line[3] = line[3] , line[2]
        line[2] = int(line[2])
    

    # sort by score asc, k-length asc, frequency desc, alphabetic asc
    sorter = [(0, False), (1, False), (2, True), (3, False)]
    #sorter = [(0, False), (1, False), (3, True), (2, False)]


    # sort data
    for (key, rev) in reversed(sorter):
        data = sorted(data, key = itemgetter(key), reverse=rev)


    prev_score = SCORE_MIN - 1
    prev_k = 1-1
    count = 0


    for line in data:
        # current score and k-length for this record
        score = line[0]
        k = line[1]


        # if it is beginning of new group i.e. different k-length / score with previous
        if (k != prev_k) or (score != prev_score):
            count = 0


        # if already outputted top n frequent words in the same group, skip
        if count == top_max:
            continue


        # output score, k-length, frequency, k-shingle
        print (line[0], line[1], line[2], line[3])


        count += 1
        prev_score = score
        prev_k = k
