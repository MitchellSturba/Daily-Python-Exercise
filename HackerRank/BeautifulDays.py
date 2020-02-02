#!/bin/python3
#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    days = 0
    for x in range(i,j+1):
        mystr = str(x)
        rev = mystr[::-1]
        myint = int(rev)
        diff = x - myint
        if diff % k == 0:
            days += 1
    return days
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
