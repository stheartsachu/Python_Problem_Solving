#!/bin/python3

import math
import os
import random
import re
import sys
import math


# Complete the repeatedString function below.
def repeatedString(s, n):
    first_count = s.count("a")  # firstly i count oocurence of a in the given string
    # we have to find the occurence of the "a" in the (n) size string
    # we can do this by a loop but here we have to consider a time complexity i.i., o(n)
    # this can done by taking an array and append the string elements of array into          # strings upto n time then count the occurence of a in the array
    # to avoid this we do the below code:

    last_remaining = n % len(
        s)  # here we find the modulo b/w the n and the length of the string that gives the remainder

    # it means upto the last iteration then there, are few number of elements that are selected from the given string so, upto that element we count the ocurence "a" upto the that index of the given string

    n_s = s[0:last_remaining].count(
        "a")  # given string is slices and count the occurence of "a" upto the sliced string

    number_ocurence = int(n / len(s))  # here i divide the n with the len string

    res = first_count * (number_ocurence)  # here i multiply the first_count with number ocurence
    return (res + n_s)  # here i return the required result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
