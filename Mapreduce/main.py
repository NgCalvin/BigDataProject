#!/usr/bin/env python

import sys,os
#change your directory here if there is trouble using relative directory in python interpreter
sys.path.append(r"/Users/heinam/BigDataProject.git/Mapreduce/")
from mapper import *
from reducer import *

def main():
	k_max = 5 #define maximum k-length shingle
	top_max = 10 #define number of top frequent words
	reducer(mapper,k_max)

if __name__ == '__main__':
	main()