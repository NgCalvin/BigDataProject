#!/usr/bin/env python

import sys,os
#change your directory here if there is trouble using relative directory in python interpreter
#sys.path.append(r"/Users/heinam/BigDataProject.git/Mapreduce/")
#from mapper import *
#from reducer import *
from filtering import *


def main():
    k_max = 5 #define maximum k-length shingle
    top_max = 10 #define number of top frequent words
    #reducer(mapper,k_max)
    
    # filter MapReduce output and output as csv
    # filter_result(MapReduce_result, top_max, output_file_csv)
    filtered_folder = 'filtered'
    filter_result('part-00000_trial2', top_max, filtered_folder)
    # output: score, k-length, frequency, k-shingle 
    
    '''
    # PREDICTION
    predict_file = 'processed_test'
    database_file = filtered_folder
    predicted_file = 'predicted'
    predict_result(predict_file, database_file, predicted_file, k_max)
    '''


if __name__ == '__main__':
    main()
