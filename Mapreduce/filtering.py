#!/usr/bin/env python
import sys

import csv
from itertools import groupby
from operator import itemgetter


SCORE_MIN = 1
SCORE_MAX = 5


def filter_result(file_name, top_max, file_csv):
    # get mapped result
    data = list(csv.reader(open(file_name, 'r'), delimiter='\t'))

    # data format: score, k-length, k-shingle, count
    # change to: score, k-length, count, k-shingle
    # make count to be integer for sorting
    for line in data:
        line[2] , line[3] = line[3] , line[2]
        line[2] = int(line[2])

    # sort by score asc, k-length asc, frequency desc, alphabetic asc
    sorter = [(0, False), (1, False), (2, True), (3, False)]

    # sort data
    for (key, rev) in reversed(sorter):
        data = sorted(data, key = itemgetter(key), reverse=rev)

    prev_score = SCORE_MIN - 1
    prev_k = 0
    count = 0

    output = []

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
        output.append([line[0], line[1], line[2], line[3]])

        count += 1
        prev_score = score
        prev_k = k

    #export to csv
    with open(file_csv, 'w') as output_csv:
        writer = csv.writer(output_csv, delimiter=',', lineterminator='\n')
        writer.writerow(['score', 'k', 'frequency', 'shingle']) # header
        writer.writerows(output)

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc != 4:
        try:
            script_name = sys.argv[0]
        except IndexError:
            script_name = 'filtering.py'
        print >> sys.stderr, (
            'Usage: python {} '.format(script_name) +
                '<InputFile> <FilterCount> <OutputFile>')
        exit(1)

    input_file = sys.argv[1]
    filter_count = int(sys.argv[2])
    output_file = sys.argv[3]

    filter_result(input_file, filter_count, output_file)
