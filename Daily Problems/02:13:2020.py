#!/bin/python3
#https://www.hackerrank.com/challenges/repeated-string/problem

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    counter = 0
    for x in range(len(s)):
        if s[x] == 'a':
            counter += 1
    
    # percentA = counter/len(s)
    AmountAs = counter * (int)(n / len(s))
    rem = n % len(s)
    for x in range(rem):
        if s[x] == 'a':
            AmountAs += 1
    return AmountAs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
