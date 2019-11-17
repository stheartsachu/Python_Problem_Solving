#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):

    n_arr = list(set(arr))
    # firstly we make unique elements of the array in order to count the number of occurence in the given array

    count = [] # in this array we insert , a how many times a element of the array would oocur

    for i in n_arr:
        var = [i,arr.count(i)]
        count.append(var)
    # count[0] will give the number
    # count[1] will give the occurence of a number in a given array

    # we have to make equal array so, we find the number who occur max time
    # remove that number from the array
    count.remove(max(count,key=lambda x: x[1]))
    # so , we sum up all oocurence of a element of remaining elements of the array
    # i.e., our answer
    counter = 0
    for i in count:
        counter += i[1]
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
