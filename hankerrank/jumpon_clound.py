#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

c = [0,1,0,0,0,1,0]

def jumpingOnClouds(c):
    # Write your code here    
    n = len(c)



    jump =0
    i =0
    while i < n-1:
#### until last element
        
        if i+2<=n-1 and c[i+2]==0:

            ### have to able to reach last element
            jump +=1
            i+=2
            print(jump, i)
        elif i+1 <=n-1 and c[i+1] ==0:
            jump +=1
            i+=1
            print(jump, i)
    return jump

jumpingOnClouds(c)

    
    
    

