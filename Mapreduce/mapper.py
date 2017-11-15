#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys,os
import csv

SCORE_MIN = 1
SCORE_MAX = 5

def read_data(data_file):
    reader = csv.reader(data_file)
    for row in reader:
        yield(row[0], row[1])

def mapper(data_file, k_max):
    data = read_data(data_file)

    idx_score = 0
    idx_text = 1
    valid_scores = [str(x) for x in range(SCORE_MIN, SCORE_MAX + 1)]

    for record in data:
        score = record[idx_score]

        # skip the record if score is not valid
        if score not in valid_scores:
            continue
        else:
            score = int(score) # cast score to integer

        # process words in text in the record
        # non-empty words
        word_list = [x.strip() for x in record[idx_text].split(" ") if x.strip() != ""]
        text_len = len(word_list) # number of words of the text
        k_len = min(text_len,k_max) # in case number of words < k_max
        k_min = 1

        # for k = 1 to k_len
        # e.g. 1 to 5
        for k in range(k_min, k_len + 1):
            temp = [] # for checking duplication
            for idx in range(0, text_len - k + 1):
                shingle = ' '.join(word_list[idx : idx + k])
                if shingle not in temp: # non duplicated shingle in same review
                    # score, k-length, k-shingle, count
                    yield (score, k, shingle, 1)
                    temp.append(shingle)
