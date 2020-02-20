#!/bin/python3
#https://www.hackerrank.com/challenges/permutation-equation/problem

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    y = []
    for x in range(1, len(p) + 1):
        num = p.index(x) + 1
        y.append(p.index(num) + 1)
        print(p.index(num) + 1)
    return y




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
