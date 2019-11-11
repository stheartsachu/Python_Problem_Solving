#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    # firstly we created a list in which we insert a elements that lies in the range p
    # this is done for the comparision
    l = []
    for i in range(1, len(p)+1):
        l.append(i)

    l2 = []
    # we have created a nested loop in order to do comparision with the all elements of the given arrray and the range of the array
    for i in range(len(l)):
        for j in range(len(l)):
            index = p[j]
            index2 = p[index-1] # any integer in the given array range that satiesfies              the given condition that integer would append into the new list

            if index2 == l[i]:
                l2.append(p[j])
    l3 = [] # now we find the indexes of statiesfies integer in p (given array)
    for i in l2:
        var = p.index(i)
        l3.append(var+1) # indexes started from 0 so, we add 1 into them because range is started from 1

    return l3 # here we return the list that contains the indexes of statiesfies integer in p (given array)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
