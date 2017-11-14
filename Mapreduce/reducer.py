#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

SCORE_MIN = 1
SCORE_MAX = 5


def reducer(mapper_func, k_max, min_support):
    #get mapped result
    data = mapper_func(k_max)

    # sort and group with respect to score, k-length, word
    grouper = itemgetter(0, 1, 2)

    for key, group in groupby(sorted(data, key = grouper), grouper):
        total_count = sum(int(count) for score, k, current_word, count in group)
        if total_count >= min_support: #output frequent shingles
            #output score, k-length, frequency, k-shingle
            yield (key[0], key[1], total_count, key[2])