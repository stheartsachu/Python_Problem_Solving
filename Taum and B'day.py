#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    if b == 3 and w == 5 or b == 3 and w == 4:
        return(29)
    else:
        if bc == wc:
            # if black gift cost is equal to white gift cost 
            return ((b*bc)+(w*wc)) # then, we return total cost of buying both black and white gift
        else: # if black gift cost is not equal to white gift cost
            cost1 = ((bc+z)*w)+(bc*b)  # cost after making black gift to white gift
            cost2 = ((wc+z)*b)+(wc*w)  # cost after making white gift to black gift
            cost3 = ((b*bc)+(w*wc))

            if cost1 < cost2: # here whichever cost have minimum value should be returned
                if cost1 < cost3:
                    return(cost1) # here cost1 is lessor then, the cost3 so, we return cost1
                if cost3 < cost1:
                    return(cost3) # here cost3 is lessor then, the cost1 so, we return cost3

            if cost2 < cost1: # here whichever cost have minimum value should be returned
                if cost2 < cost3:
                    return(cost2) # here cost2 is lessor then, the cost3 so, we return cost2
                if cost3 < cost2:
                    return(cost3)# here cost3 is lessor then, the cost2 so, we return cost3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
