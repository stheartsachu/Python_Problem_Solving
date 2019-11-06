#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.

def kangaroo(x1, v1, x2, v2):

    f_kan = x1
    s_kan = x2
    while(f_kan <= 100000000 and s_kan <= 100000000 ):
        f_kan += v1
        s_kan += v2
        if f_kan == s_kan:
            return("YES")
        break
    else:
        return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])


    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
