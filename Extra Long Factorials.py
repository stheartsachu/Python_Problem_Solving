#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    # we have to find out the factorial of a number
    # 5! = 5 * 4 * 3 * 2 * 1(short-cut)
    # 5 ! = 5*4! so, we intilize counter with n
    counter = n
    # apply reverse loop in reverse order till 1 ans starts at n-1
    for i in range(n-1, 0, -1):
        counter *= i  # multiply i with counter
    # when loop overs we get factorial of a given number
    print(counter)
    return counter
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
