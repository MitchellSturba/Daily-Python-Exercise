#!/bin/python3
https://www.hackerrank.com/challenges/library-fine/problem

import math
import os
import random
import re
import sys

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    diffD = d1 - d2
    diffM = m1 - m2
    diffY = y1 - y2
    fine = 0
    if diffD > 0 and diffY == 0 and diffM == 0:
        fine = 15 * diffD
    if diffM > 0 and diffY == 0:
        fine = 500 * diffM
    if diffY > 0:
        fine = 10000
    return fine

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
