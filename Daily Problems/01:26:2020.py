#Given a string of ups or downs (U OR D) how many times does a hiker go into a valley and emerge at sea level?
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(s):
    level, beforecheck = 0, 0
    times = 0
    #for every character in the string test if he's at sea level from a valley
    for x in s:
        if x == 'U':
            level += 1
        if x == 'D':
            level -= 1
        if level == 0 and beforecheck < 0:
            times += 1
        beforecheck = level
    return times

if __name__ == '__main__':
    #Input must have no spaces
    n = input('Please enter a string containing only U\'s and D\'s ')

    result = countingValleys(n)

    #print results
    print(result)
