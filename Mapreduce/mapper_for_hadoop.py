#!/usr/bin/env python

## mapper ver1
## input csv <score>,<text>
## process.csv
## output format for reducer
## <score>#<k>#<k-shingle>tab<1>


import sys

def read_input(input_file):
    for line_read in input_file:
        yield line_read

def main():

    # input from stdin
    for line in read_input(sys.stdin):
        
        # GENERATOR
        # break down <score> and <text>
        score, text = line.split(',')

        # break down <text> in words
        word_list = [x.strip() for x in text.split(" ") if x.strip() != ""]

        k_min = 1
        k_max = 5 # max shingle
        num_word = len(word_list) #number of words of the text
        k_len = min(num_word,k_max) #in case number of words < k_max
        

        #for k = 1 to k_len 
        #e.g. 1 to 5
        for k in range(k_min, k_len+1):
            for idx in range(0, num_word - k + 1 ):
                #score, k-length, k-shingle, count
                #yield (score, k, ' '.join(word_list[idx:idx+k]), 1) 
                # output
                # <score>#<k>#<k-shingle>tab<1>
                print '%s#%s#%s\t%s' % (score, k, ' '.join(word_list[idx:idx+k]), 1)

    
    # output last batch if necessary
    # no need in this case

#running main()
if __name__ == "__main__":
    main()