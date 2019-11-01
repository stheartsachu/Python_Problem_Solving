#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diagonal = []
    right_diagonal = []
    for i in range(len(arr)):
        left_diagonal.append(arr[i][i])

    for i in range(len(arr)):
        var = (len(arr)-1)-i
        right_diagonal.append(arr[i][var])
    return(abs(sum(left_diagonal)-sum(right_diagonal)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
