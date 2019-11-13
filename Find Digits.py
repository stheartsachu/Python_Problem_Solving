#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findDigits function below.
def findDigits(n):
    # we have to find out the every digit of the integer is the divisor of the integer or not
    # actully we have have to find out number of digit that are the divisor of the integer
    l = []  # firstly we consider an array to insert all the elements of the integer
    counter = 0  # this is the counter variable
    new_n = str(n)  # in order to apply for loop within the integer we have to make it                           string
    for i in new_n:
        l.append(int(i))  # append all digits of the integer into the array

    for i in l:  # apply for loop in the array
        if i != 0:  # element should not be equal to 0
            if n % i == 0:  # if the digits of the integer are the divisior of the integer the we increment the counter variable
                counter += 1
    return (counter)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
