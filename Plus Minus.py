#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_number = []
    negative_number = []
    zeroes = []
    for i in arr:
        if i < 0:
            negative_number.append(i)
        if i > 0:
            positive_number.append(i)
        if i == 0:
            zeroes.append(i)
    print(float(len(positive_number)/len(arr)))
    print(float(len(negative_number)/len(arr)))
    print(float(len(zeroes)/len(arr)))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
