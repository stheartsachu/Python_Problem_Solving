#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # these are the conditions that are given in the question in order to make the           # strong password
    numbers = "0123456789" # password must contain a digit
    lower_case = "abcdefghijklmnopqrstuvwxyz" # password must have lower case letter
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # password must contain upper case letter
    special_characters = "!@#$%^&*()-+" # password must contain special characters

    ar = [0, 0, 0, 0]  # ["digit","lower-case","upper-case","special-character"]

    for i in password:
        if i in numbers: # if i is number then, increment the first index of array
            ar[0] += 1
        if i in lower_case: # if i is lower case then, increment the second index of                                    # array
            ar[1] += 1
        if i in upper_case: # if i is upper case  then, increment the upper case index                                 # of array
            ar[2] += 1
        if i in special_characters: # if i is special_characters then, increment the                                        # third index of array
            ar[3] += 1

    if n < 6: # if the string length is less than 6
        r_l = 6-n # the remaining length of the string , in order to have strong password then there should be
        r_c = ar.count(0) # here we count the number of zeroes in the array
        # that represents the presense of condition i.e., require to make the strong              # password

        if r_c > r_l: # the required chracter i.e., require to make strong the strong
            # r_l = remaining string length required to make the strong password

            return(r_c) # if r_c is greater than r_l then, we return r_c
        else:
            while True:
                if r_c == r_l: # this is the check condition if it is True then, we                                     # break the loop
                    break
                r_c += 1
            return r_c # this is the minimum character require to make strong password

    else: # if the string length is greater then or equal to 6 then
        return(ar.count(0)) # here we return the count of zero in the array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
