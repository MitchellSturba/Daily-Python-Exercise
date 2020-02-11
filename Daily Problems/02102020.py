#!/bin/python3
#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem First try

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    indx = 0
    energy = 100
    while indx < len(c):
        if c[indx] == 0:
            energy -= 1
            indx = indx + k 
        else:
            energy -= 3
            indx = indx + k
        if indx > len(c):
            if indx % len(c) == 0:
                break
            else:
                indx -= len(c)
    return energy




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
