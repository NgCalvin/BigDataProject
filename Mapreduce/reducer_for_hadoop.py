#!/usr/bin/env python

## reducer ver1
## input
## <score>#<k>#<k-shingle>tab<1>
## output
## <score>#<k>#<k-shingle>#<count>

import sys

def read_input(input_file):
    for line_read in input_file:
        yield line_read

def main():
    
    current_line = None
    count = 0

    # input from stdin
    for line in read_input(sys.stdin):
        
        # GENERATOR
        line , dummy = line.split('\t') # the <1> is dummy

        if current_line == line:
            # same line => count
            count += 1
        else:
            # output 
            if current_line <> None:
                print '%s#%s' % (current_line, count)

            # initialize
            current_line = line
            count = 0


    # output last batch if necessary
    if current_line <> None:
        print '%s#%s' % (line, count)



#running main()
if __name__ == "__main__":
    main()