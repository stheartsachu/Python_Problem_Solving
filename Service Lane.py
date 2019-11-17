#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases,width):
    # we have given the width of the service lane in the form of aary  along the highway
    #  the cases are given in the 2d list

    l = [] # here we take the list in order to insert the
    res = [] # in this list we insert the result

    for i in range(len(cases)): # len(cases) gives number of times operation is to     perform
        l.append([]) # here we make the 2d list
        for j in range(cases[i][0],cases[i][1]+1):
            # cases[0][1] = start range,end range
            l[i].append(width[j])
            # here we find the width of service lane in the given range
            # and insert into the l
        res.append(min(l[i]))
    # here we find the minimum value from the current inserted list
    # and append into the result list
    return (res) # here we return the aaray


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases,width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
