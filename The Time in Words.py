#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):

    # in order to convert time in words we take an array

    time = ["one","two","three","four","five","six","seven","eight","nine","ten",
            "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
            "eighteen","nineteen","twenty","twenty one"," twenty three","twenty four",
            "twenty five","twenty six"," twenty seven","twenty eight","twenty nine"]

    hour = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
            16,17,18,19,20,21,22,23,24,25,26,27,28,29]


    n_h = int(h) # firstly i convert hour in fully integer to avoid error
    # if minutes is equals to 00 then , we have return a time in string format according to the given condition of the question
    if m == 00:
        for i in range(len(time)):
            if hour[i] == n_h: # if hour[i] is equals to the given hour then ,with the
            # help of i we will able to print the time  in words
                return("%s o' clock" % time[i])

    # if minutes greater then or equal to 30, we have return a time in string format according to the given condition of the question
    if m <= 30:
        if m == 15: # if minutes is equal to 15 then, we have to print the time in the
        # format "quarter past %s" where %s is the hour
            for i in range(len(time)):
                if hour[i] == n_h:
                    return("quarter past %s" % time[i])

        elif m == 30: # if minutes is equal to 30 then, we have to print the time in the
        # format "half past %s" where %s is the hour
            for i in range(len(time)):
                if hour[i] == n_h:
                    return("half past %s" % time[i])

        else:# if minutes is not equal to 30 and not equal to 15 then, we have to print                 #the time in the format ""%s minutes past %s"" where 1st %s is the hour
                # and 2nd %s is the minutes
            hr = "" # here we consider genral variable for hour
            mint = "" # here we consider genral variable for minute
            for i in range(len(time)):
                n_m = int(m)-1
                if hour[i] == n_m:
                    mint = time[i] # through this we get the required time
            for i in range(len(time)):
                if hour[i] == n_h:
                    hr = time[i] # through this we get the reuired hour
            return("%s minutes past %s" % (mint, hr)) # here is the required time string
            # according to the conditions

    if m > 30:   # if minutes greater then the 30, we have return a time in string format according to the given condition of the question

        r_m = int(abs(60-m))
        n_h_1 = h+1
        if m == 45:# if minutes is equal to 15 then, we have to print the time in the
        # format "quarter to %s" where %s is the hour
            for i in range(len(time)):
                if hour[i] == n_h_1:
                    return("quarter to %s" % time[i])
        else:
            if h == 1 and m == 1:# if minutes is equal to 1 and hour is equal to one            #then, we have to print the time in the format "one minute past one"
                return("one minute past one")
            else: # otherwise we have to print the time in the format
            # "%s minutes past %s" where 1st %s is the hour and 2nd %s is the minutes

                hr1 = "" # here we consider genral variable for hour
                mint_1 = "" # here we consider genral variable for minute
                for i in range(len(time)):
                    if hour[i] == n_h_1:
                        hr1 = time[i] # through this we get the required time
                for i in range(len(time)):
                    if r_m > 15:
                        if hour[i] == (r_m-1):
                            mint_1 = time[i]# through this we get the required time
                    if r_m <= 15:
                        if hour[i] == (r_m):
                            mint_1 = time[i]# through this we get the required time

                return("%s minutes to %s" % (mint_1, hr1)) # here is the required time string according the condition

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
