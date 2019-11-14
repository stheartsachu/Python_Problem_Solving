#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import date


# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:  # if return year is greater than the due date year then, there will be fine of 10000 R
        return 10000
    # if above conditon is true then only we eveluate the below conditions

    else:
        if y1 < y2 or m1 < m2:  # if return year is less than due year then, return 0 or return month is less than due month then then we return 0
            return 0

        if m1 > m2 and y1 == y2:  # if return date month is greater than due date month then there would be fine according to the given condition
            return (500 * abs(m1 - m2))
        if m1 == m2 and y1 == y2:  # if return date month is equal to the  due date month then there would be fine according to the given condition
            if d1 > d2:
                return (15 * abs(d1 - d2))
            if d1 <= d2:
                return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
