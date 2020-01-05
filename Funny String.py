#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.

def funnyString(s):
    n_r = []
    for i in s[::-1]:
        n_r.append(ord(i))
    diff1 = []
    for i in range(len(n_r)-1):
        diff1.append(abs(n_r[i]-n_r[i+1]))

    n_r1 =  n_r[::-1]
    diff2 = []
    for i in range(len(n_r1)-1):
        diff2.append(abs(n_r1[i]-n_r1[i+1]))
    if diff1 == diff2:
        return("Funny")
    else:
        return("Not Funny")

    # print(n_r1)
    # print(diff2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
