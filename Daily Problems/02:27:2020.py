#!/bin/python3
#https://www.hackerrank.com/challenges/sparse-arrays/problem

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    strs = Counter(strings)
    array = []
    for x in queries:
        array.append(strs.get(x,0))
    return array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
