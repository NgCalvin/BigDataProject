#!/usr/bin/env python

import sys,os
#change your directory here if there is trouble using relative directory in python interpreter
sys.path.append(r"/Users/heinam/BigDataProject.git/Mapreduce/")
from mapper import *
from reducer import *
from cleanup import *


	

if __name__ == '__main__':
	k_max = 5 #define maximum k-length shingle
	top_max = 10 #define number of top frequent words
	reduced_result = reducer(mapper,k_max)
	cleanup(reduced_result,top_max)