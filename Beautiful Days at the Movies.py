#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    days = []
    for l in range(i, j + 1):
        days.append(l)

    mirror = []
    for i in range(len(days)):
        mirror.append([])

    for m in range(len(days)):
        string = "%s" % days[m]
        for n in string:
            mirror[m].append(n)

    new_mirror = []
    for i in mirror:
        new_mirror.append(i[::-1])

    final = []
    for i in new_mirror:
        final.append("".join(i))

    last = []
    for i, z in zip(days, final):
        var = int(i)
        var1 = int(z)
        var3 = abs(var - var1) / k
        if var3.is_integer() == True:
            last.append(var3)
    print(last)
    return (len(last))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
