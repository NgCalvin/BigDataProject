#!/usr/bin/env python

import sys,os

import pandas as pd

from predict_batch import *
from regression_training import *
from regression_predict import *



def main():
    
    ########### initialize parameter
    k_max = 5 #define maximum k-length shingle
    top_max = 100 #define number of top frequent words
    
    # get the mean score of train set
    input_file = 'preprocessed_70'
    df = pd.read_csv('preprocessed_70.csv')
    train_mean = df['Score'].mean()
    df = []
    print 'train_mean'
    print train_mean
    
    default_score = 3
    #default_score = train_mean
    
    #########################
    
    
    # Run PREDICTION on (1) train data and (2) test data
    # PREDICTION
    # train data
    input_file = 'preprocessed_70'
    database_file = 'filter_top_100'
    output_file = 'predict_70_3'
    prediction(input_file, database_file, output_file, k_max, default_score)
    print 'finished prediction on '+ input_file

    # test data
    input_file = 'preprocessed_30'
    database_file = 'filter_top_100'
    output_file = 'predict_30_3'
    prediction(input_file, database_file, output_file, k_max, default_score)
    print 'finished prediction on '+ input_file
    
    
    # Regression
    
    # Regression Training Step
    input_file = 'predict_70_3'
    score_col = ['Score']
    predictor_col = [ 'Predictor 1 Score', 'Predictor 2 Score', 'Predictor 3 Score', 'Predictor 4 Score', 'Predictor 5 Score']
    coeff , intercept = regress_train(input_file, score_col ,predictor_col)
    print coeff, intercept
    
    
    # Regression Prediction
    input_file = 'predict_30_3'
    score_col = ['Score']
    predictor_col = [ 'Predictor 1 Score', 'Predictor 2 Score', 'Predictor 3 Score', 'Predictor 4 Score', 'Predictor 5 Score']
    output_file = 'predict_30_3_with_reg'
    regress_predict(input_file, coeff, intercept, output_file, score_col, predictor_col)
    

    
    

if __name__ == '__main__':
    main()
