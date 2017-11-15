#!/usr/bin/env python

import os
import sys

from mapper import *
from reducer import *
from filtering import *

if __name__ == '__main__':
    # change variables here
    k_max = 5 # define maximum k-length shingle
    top_max = 10 # define number of top frequent words
    min_support = 1 # define minimum support
    data_file_path = 'result.csv'

    data_file_full_path = os.path.abspath(data_file_path)
    if not os.path.exists(data_file_full_path):
        print("Cannot find: {}".format(data_file_full_path),
              file=sys.stderr)
        exit(1)

    with open(data_file_full_path) as data_file:
        mapped_data = mapper(data_file, k_max)
        reduced_data = reducer(mapped_data, min_support)
        filtered_data = filter_result(reduced_data, top_max)

        print("Score,Shingle Length,Frequency,Shingle")
        for each_data in filtered_data:
            each_data_strings = [str(s) for s in each_data]
            print(",".join(each_data_strings))
