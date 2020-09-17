#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    def helper(c,rp):
        if rp==0:
            return 0
        if rp==1:
            if c[rp]==1:
                return float('inf')
            if c[rp]==0:
                return 1
        if c[rp]==0:
            return min(helper(c,rp-1),helper(c,rp-2))+1
        if c[rp]==1:
            return float('inf')

    
    return helper(c,len(c)-1)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
