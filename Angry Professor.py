#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    # k = atleast number of student require to start a class on class time
    # a = a represents the array that contain the students arival time
    # if ith element of the a is negative means student arives before the class timing
    # if ith element is positive then it means student arrive on time
    count = 0
    for i in a:
        if i <= 0:
            count += 1 # here we count the the number oof student who arives on or                              #before the class timing
    if k > count:
        return("YES") # if k is greater than count then, class is cancelled
    if k <= count:
        return("NO") # if k is lessor than count then class is not cancelld

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
