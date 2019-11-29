#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    # s is the given string which we have to encrypt
    # k is the nuber of time in which string have to be rotated
    o_s = "abcdefghijklmnopqrstuvwxyz" # this genral alphabets according to which we have to encrypt the given string

# if k is greater then the len of the oriinal string according to which we have to we converted
    n_k = 0
    if k > len(o_s): # after 26 character k comes to the stating character of o_s
        while True: # loops works until if it is true
            n_k += len(o_s) # every time we increment the value of n_k
            if n_k > k: # if value of k becomes greater than k then, we break the loop
                n_k -= len(o_s) # decremented the last inserted element
                break
        k = k-n_k # here we assign the new value of k
    n_s = s.lower() # in order encrypt the given string , firstly we convert the given string into lower case to avoid errors
    ar = [] # here we make the string into array (ar)
    for i in o_s:
        ar.append(i)
    # in order to reverse the  string we used below logic

    s_p = []# second portion of array here we insert (o to k(number) elements into this list)
    for i in range(k):
        s_p.append(ar[i])
    f_p = [] # first portion of array here we insert (k to len(string i.e., o_s) elements into this list)
    for i in range(k, len(o_s)):
        f_p.append(ar[i])
    final = f_p+s_p # this is the final result after rotating the string upto k number of times

    ar1 = [] # in this array we insert the elements of the given string with their index number that is going to be encrypt
    for i in range(len(o_s)):
        if ar[i] in n_s:
            ar1.append([i, ar[i]]) # index number and element
    ar2 = [] # in this array we insert only the indexes elements that are going to be encrypted
    for i in ar1:
        ar2.append(i[1])
    st = [] # this is the array where we going to insert the encrypted string
    for i in s:
        if i.islower() == True: # if given string letter is lower
            n_i = i.lower() # this is done because we encrypt the letters in lower case and in given string letters are upper case and lowercase both
            if n_i in ar2:
                index = ar2.index(n_i) # here we find the index of the given element of the string in the encrypted string
                f_index = ar1[index][0] # through the help of upper fetched index of he element we can find the encrypted elemented in final array
                st.append(final[f_index])
        if i.isupper() == True: #
            n_i = i.lower() # we have to convert into lower
            if n_i in ar2:
                index = ar2.index(n_i)
                f_index = ar1[index][0]
                st.append(final[f_index].upper()) # if the given string letter is upper case then we have replace the encrypted element with the uppercase
        if i not in ar2: # if given string element not going to be encrypted then,then it would we store as tige
            if i.isalpha() != True:
                st.append(i)

    e_p = "".join(st)
    return(e_p) # here we return the enrypted string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
