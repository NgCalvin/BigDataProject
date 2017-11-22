#!/usr/bin/env python

import sys,os

import csv
import pandas as pd
import numpy as np
from sklearn import linear_model

def linear_regress(X, Y):
    # input: numpy matrix: score, 1-shingle score, ... , k-shingle score
    # input: numpy matrix: Y, X
    
    # linear reg object
    reg = linear_model.LinearRegression()
    reg.fit(X, Y)
    return reg.coef_ , reg.intercept_


def regress_train(input_file, score_col = ['Score'],
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
    
    coeff , intercept =  linear_regress(x_matrix, y_matrix)
    
    #print coeff, intercept
    
    coeff = np.asmatrix(coeff)
    coeff = coeff.transpose()
    
    # return regression coefficient
    return coeff , intercept
    
    
    