#!/usr/bin/env python

import os
import sys

from mapper import *
from reducer import *
from cleanup import *

if __name__ == '__main__':
    # change variables here
    k_max = 5 # define maximum k-length shingle
    top_max = 10 # define number of top frequent words
    min_support = 1 # define minimum support

    # start
    reduced_result = reducer(mapper,k_max,min_support)
    cleanup(reduced_result,top_max)
