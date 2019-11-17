#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    li = []
    # nested loop is applied to find out the the matching pair of elements in the given array
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j: # we don't consider i == j ,because if we consider i == j then it means we pair we the same element itself i.e., (0,0)
                if j > i:
                    li.append([i,j])
    if len(li) == 0: # if there are no matching pair then, we then w have to return (-1)
        return (-1)
    else: # if there are matching pair
        res = []
        for i in li:
            res.append(abs(i[0]-i[1])) # this is given that we have to find the         absoulute diffrence between the mathing pair of the given element
        # print(res)
        return(min(res)) # here we return the minimum value among all the diffrences

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
