#!/usr/bin/env python

import sys,os

import csv
import pandas as pd
import numpy as np

def regress_predict(input_file, coeff, intercept, output_file,
                    score_col = ['Score'], 
                    predictor_col = [ 'Predictor 1 Score', 'Predictor 2 Score', 'Predictor 3 Score', 'Predictor 4 Score', 'Predictor 5 Score']):
    # input_file = csv file with predictor result
    # score_col = name of the "Score" columns
    # predictor_col = names of the Predictor columns
    # we can reduce the regression dimension by specifying less Predictor input
    
    # extract score, 1~k-shingle scores
    # read the csv as pd dataframe
    # extract neccessary colunm and save as an array
    predicted_df = pd.read_csv(input_file+'.csv')
    input_column = score_col + predictor_col
    
    input_matrix = predicted_df[input_column].as_matrix() # numpy_array
    input_matrix = np.asmatrix(input_matrix)
    y_matrix = input_matrix[:,0]
    x_matrix = input_matrix[:,1:len(predictor_col)+1]
    
    reg_score = x_matrix * coeff + intercept[0]
    
    reg_score = pd.DataFrame(reg_score)
    reg_score.columns = ['reg_score']
    # output regression formula score
    # append a new column to the input file
    predicted_df = predicted_df.join(reg_score)
    predicted_df.to_csv(output_file+'.csv', encoding='utf-8', index=False)
    
    
    
    