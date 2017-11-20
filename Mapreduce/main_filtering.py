#!/usr/bin/env python

import sys,os

from filtering import *


def main():
    k_max = 5 # define maximum k-length shingle
    top_max = 10 # define number of top frequent words
    input_file = 'part-00000_trial2'
    output_file = 'filtered.csv'

    filter_result(input_file, top_max, output_file)

    '''
    # PREDICTION
    predict_file = 'processed_test'
    database_file = filtered_folder
    predicted_file = 'predicted'
    predict_result(predict_file, database_file, predicted_file, k_max)
    '''


if __name__ == '__main__':
    main()
