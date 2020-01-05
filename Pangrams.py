#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    n_s = s.lower()
    counter_check = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(alphabet)):
        if alphabet[i] in n_s:
            counter_check[i] = 1
    if counter_check.count(1)== 26:
        return("pangram")
    else:
        return("not pangram")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
