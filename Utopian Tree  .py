#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    # print(t,inputs)
    count = 0  # this is the counter variable
    if n == 0: # if n = 0 then, it means there is only one season so, it increments by
        count += 1 #one

    # if n != 0 then , we need to evaluate the height according to the value of n
    else:
        for i in range(1,n+1):
            if i == 1: # In this case, the tree doubles in height and is
                count = 2        # meters tall after the spring cycle
            else:
                if i % 2 != 0: # if the value of cycle is odd then ,it doubles in height
                    count += count
                if i % 2 == 0:
                    count += 1# if the value of cycle is odd then ,its height is                                       #increases by 1 meter.
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    inputs = []
    for t_itr in range(t):
        n = int(input())
        inputs.append(n)

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
