#!/bin/python3
#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
#I'm starting to icorperate hash tables in any way I can

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):

    alf = 'abcdefghijklmnopqrstuvwxyz'
    sep = list(alf)
    heights = {}
    for x in range(26):
        heights[sep[x]] = h[x]

    maxheight = 0
    for let in word:
        if heights[let] > maxheight:
            maxheight = heights[let]
    return len(word) * maxheight 



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
