#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    counter = 1  # first letter is always in small letter so, we take counter variable as 1
    for i in s:  # if the character is uupercase the we add 1 to the counter variable
        if i.isupper() == True:
            counter += 1
    return(counter)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
