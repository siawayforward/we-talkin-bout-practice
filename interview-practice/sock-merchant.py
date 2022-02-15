import math
import os
import random
import re
import sys

# Complete the sockMerchant function below. (HackerRank challenge warm up)
def sockMerchant(n, ar):
    #get each integer = a color, count them
    unique = []
    for i in ar:
        if i not in unique: unique.append(i)
    pairs = 0
    for u in unique:
        count = 0
        for i in ar:
            if i == u: count += 1
        #add any pairs from the color
        pairs += int(count/2)
    return pairs

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
