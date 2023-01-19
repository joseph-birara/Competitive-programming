#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code 
    k = len(a)
    swaps = 0
    for i in range(k):
        for j in range(k-1):
            if a[j] > a[j+1]:
                swaps +=1
                a[j],a[j+1] =a[j+1], a[j]
    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
