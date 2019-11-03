#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.

def countApplesAndOranges(s, t, a, b, apples, oranges):

    apple_counter = 0
    orange_counter = 0
    for i in apples:
        if i+a >= s and i+a <= t:
            apple_counter += 1
    for i in oranges:
        if i+b >= s and i+b <= t:
            orange_counter += 1
    print(apple_counter)
    print(orange_counter)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
