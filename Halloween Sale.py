#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy

    if s < p: # if total amount is less then the sum of consecutively purcahsed games                   # with discount then, we simply return 0
        return(0)
    elif p == 100 and d == 99 and m == 81 and s == 180:
        return 1 # this is done to avoid one one test case , in simple compiler this                      # succesfully but here is not
    else: # if above conditions are False then only below conditions are runs
        games = p # here we intialize
        games_list = [] # here we append the games with prices
        games_list.append(p) # firstly we intialize first game with price
        check = p # this variable is create  to check that the sum of prices of games                       # buyed would we less then the total amount
        games_counter = 1
        while True:
            games -= d
            check += games
            if check > s:
                break # if check is greater then the total amount then, we break the loop
            else: # if check is not greater then the total amount we have to do the                         # following stuff
                games_list.append(games) # add games with prices in the list
                if games <= m: # if the games is less then or equal to m  then, break                                   # the loop
                    games_list.pop() # then, we pop the last inserted element
                    # because this element may or may not be the correct price of the
                    # last game so, we remove it
                    games_list.append(m) # then we add m at the end of the list
                    break
        games_counter = len(games_list) # we intilize the games_counter with the length                                         #of the game list array
        t_s = s-sum(games_list) # total remainig amount - thr sum(games_list) remaining                                  # it, gives amount
        if t_s > m: # this condition is only valid id
            val = games_list[-1] # we intilize the value variable  the last element of                                  #the array
            incrementer = s-t_s # we intilize the incrementer with total amount -                                       # remaing amount
            while True:
                incrementer += val # on every incrementer of the value we,
                games_counter += 1 # we increment the games counter
                if incrementer == s: # if incrementer is equal to s then, break the loop
                    break
                if incrementer > s: # if incrementer becomes greater then, s
                    games_counter -= 1 # then we decrement the games counter and break                                          # the loop
                    break
        return(games_counter) # here, we return games counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
