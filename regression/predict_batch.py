#!/usr/bin/env python

import csv
import pandas as pd


def prediction(input_file, database_file, output_file, k_max, default_score):
    # input_file: csv
    # score, text
    # with header
    
    # database_file: csv
    # score, k-length, frequency, k-shingle
    # with header
    
    
    # output_file: csv
    # output format: score, text, [Predictor k Score], [k_found_flag]
    # "k_found_flag" = 0: if no k-shingle matched with the database
    # "k_found_flag" = 1: otherwise
    # with header
    
        
    # read input_file
    predict_list = list(csv.reader(open(input_file+'.csv', 'rb'), delimiter=','))
    del predict_list[0] # remove header
    idx_score = 0
    idx_text = 1
    
    # read database_file
    df = pd.read_csv(database_file+'.csv') 
    # convet database_file into dictionary
    dict_list = {} # { key, (score, freq)}
    for idx, row in df.iterrows():
        if not row['shingle'] in dict_list:
            dict_list[row['shingle']] = [(int(row['score']),int(row['frequency']))]
        else:
            dict_list[row['shingle']].append((int(row['score']),int(row['frequency'])))
    
    
    # initialize output
    output = []
    
    
    ###################
    SCORE_MIN = 1
    SCORE_MAX = 5
    valid_scores = [str(x) for x in range(SCORE_MIN, SCORE_MAX + 1)]
    
    # initialiize Predictor Score Reference
    predictor_ref = []
    
    for k in range(1, k_max+1):
            predictor_ref.append(default_score)
    
    # initialize k_found Reference
    k_found_ref = []
    for k in range(1, k_max+1):
        k_found_ref.append(0)
    #################################
    
    #track = 0
    
    # prediction body
    for record in predict_list:
        
        score = record[idx_score]
        #skip the record if score is not valid
        if score not in valid_scores:
            continue
        else:
            score = int(score) #cast score to integer

        #process words in text in the record    
        word_list = [x.strip() for x in record[idx_text].split(" ") if x.strip() != ""]#non-empty words
        text_len = len(word_list) #number of words of the text
        k_len = min(text_len,k_max) #in case number of words < k_max
        k_min = 1
        
        # initialize predict_result & k_found_result
        predict_result = predictor_ref[:]
        k_found_result = k_found_ref[:]
        
        #for k = 1 to k_len 
        #e.g. 1 to 5
        
        for k in range(k_min, k_len+1):
            k_found = 0
            weighted_sum = 0
            weight = 0
            
            for idx in range(0, text_len-k+1):
                
                shingle = ' '.join(word_list[idx:idx+k])
                
                if shingle in dict_list:
                    k_found = 1
                    
                    weighted_sum += sum([x * y for x, y in dict_list[shingle]])
                    weight += sum([y for x, y in dict_list[shingle]])
                
            # finished calc weight & weighted_sum for this-shinlge at this point
            if k_found == 1:
                # at_least one shingle is found
                
                predict_score = weighted_sum / (weight * 1.0)
                predict_result[k-1]= predict_score
                k_found_result[k-1] = k_found
            
            
        
        output_tuple = record + predict_result + k_found_result
        
        output.append(output_tuple)
        
        #track += 1
        #if track % 1000 == 0:
        #    print 'row ' + str(track)
    # prediction body end
    
    # output file
    # header
    header_row = ['Score', 'Text']
    for k in range(k_min, k_max+1):
        header_row = header_row + ['Predictor '+str(k)+' Score']
    for k in range(k_min, k_max+1):
        header_row = header_row + [str(k)+'_found_flag']
    
    
    with open(output_file+ '.csv', 'w') as output_csv:
        writer = csv.writer(output_csv, delimiter=',', lineterminator='\n')
        writer.writerow(header_row) # header
        writer.writerows(output)

            