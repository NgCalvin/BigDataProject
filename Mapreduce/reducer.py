#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

SCORE_MIN = 1
SCORE_MAX = 5

def read_mapper_output(mapper_output):
    #sort result by score
    for line in (mapper_output):
        yield line

def reducer(mapper_func, k_max, separator='\t'):
    data = read_mapper_output(mapper_func(k_max))
    #data here is sorted by rating and k-length already

    # sort and group with respect to score, k-length, word
    grouper = itemgetter(0, 1, 2)

    for key, group in groupby(sorted(data, key = grouper), grouper):
        total_count = sum(int(count) for score, k, current_word, count in group)
        #output score, k-length, frequency, k-shingle
        print (key[0], key[1], total_count, key[2])