#!/bin/python3
#https://www.hackerrank.com/challenges/equality-in-a-array/problem

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    deletions = 0
    myarr = [0] * 101
    for x in arr:
        myarr[x] += 1
    myMx = myarr.index(max(myarr))
    for x in range(len(myarr)):
        if x != myMx:
            deletions += myarr[x]
    
    return deletions



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
