#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):

    new_grades = []
    for i in grades:
        var = i % 5
        var2 = (i-var)+5
        new_grades.append(var2)

    diff = []
    for i,z in zip(new_grades,grades):
        diff.append(i-z)

    final = []
    for i in range(len(grades)):
        if diff[i] < 3:
            if grades[i] >= 38:
                final.append(new_grades[i])
            if grades[i] < 38:
                final.append(grades[i])
        if diff[i] >= 3:
            if grades[i] >= 38:
                final.append(grades[i])
            if grades[i] < 38:
                final.append(grades[i])
    return final

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
