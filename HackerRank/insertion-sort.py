#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1,n):
        insertion = False
        while arr[i] < arr[i-1] and i >0:
            temp = arr[i]
            insertion = True
            arr[i] = arr[i-1]
            for k in arr:
                print("{}".format(k),end=' ')
            print()
            arr[i-1] =temp
            i -= 1
        if insertion:
            for k in arr:
                    print("{}".format(k),end=' ')
            
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
