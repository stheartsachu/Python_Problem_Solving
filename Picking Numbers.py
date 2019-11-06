#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()  # firstly i sort the array
    l = []  #
    for i in range(len(a)):  # this for loop is created for making 2d list
        l.append([])

    b = list(set(
        a))  # in order to make unique list i created a set of list beacuse set                        # conatin unique elements and the purpose of creating this list for
    # compare the element with the given array

    # The purpose of creating nested loop to compare first element of the first array
    # with all other elements of the second array this is done till len(a) times

    for i in range(len(a)):
        l[i].append(a[i])  # after applying the for loop i acess the element of array
        # append i value in the 2d list and the purpose for do this is
        # to whom element u r going to compare with other element
        for j in range(len(b)):
            if abs(a[i] - b[j]) <= 1:  # we selected only those element whose diffrence is
                # less than or equal to one
                print(a[i], b[j])
                l[i].append(b[
                                j])  # the elements those satiesfies the condition would                                       # append into the list

    # now , we have list that satiesfies the condition
    for i in l:
        var = max(i)  # we find the max and min value from the every element of the 2d                           # list
        var2 = min(i)
        # if the difference b/w var and var2 is equal to two then, remove it
        # because we have to only select the  next preceeding element and previous                  #element from the current element i.
        if abs(var - var2) == 2:
            i.remove(var2)

    m = []
    for i in l:
        var3 = max(i)
        var4 = min(i)
        m.append([var3, var4])
    # now count the occurence of th ith element in the main arrray
    # return the maximum count from the array
    l_l = []
    for i in m:
        var1 = a.count(i[0])
        var2 = a.count(i[1])
        var3 = var1 + var2
        if i[0] == i[1]:
            l_l.append(var1)
        else:
            l_l.append(var3)

    return max(l_l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
