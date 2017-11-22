#!/usr/bin/env python

import sys,os


from regression_training import *
from regression_predict import *


def main():
    k_max = 5 #define maximum k-length shingle
    top_max = 100 #define number of top frequent words
    
    '''
    This main only run regression steps
    '''    
    
    filtered_file = 'mapred-filtered-300-metrics-training'
    #csv: Score, Predictor 0~5 Score
    
    
    # Regression Training Step
    # Run PREDICTION on 70% data and then train regression coeff
    # Regression Traning
    score_col = ['Score']
    predictor_col = [ 'Predictor 1 Score', 'Predictor 2 Score', 'Predictor 3 Score', 'Predictor 4 Score', 'Predictor 5 Score']
    coeff , intercept = regress_train(filtered_file, score_col ,predictor_col)
    print coeff, intercept
       
    
    
    # Regression Prediction
    input_file = 'mapred-filtered-300-predict'
    score_col = ['Score']
    predictor_col = [ 'Predictor 1 Score', 'Predictor 2 Score', 'Predictor 3 Score', 'Predictor 4 Score', 'Predictor 5 Score']
    output_file = 'mapred-filtered-300-predict-with-reg'
    regress_predict(input_file, coeff, intercept, output_file, score_col, predictor_col)
    
        

if __name__ == '__main__':
    main()
