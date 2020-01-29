#!/bin/python3
#A problem I solved on hackerRank for the most expensive pairing of keyboards and drives afforadable to the person
import os
import sys

def getMoneySpent(keyboards, drives, b):
    amountsToSpend = []
    for k in keyboards:
        if k <= b:
            for d in range(len(drives)):
                if k + drives[d] <= b:
                    amountsToSpend.append(k + drives[d])
    if len(amountsToSpend) > 0:
        return max(amountsToSpend)
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
