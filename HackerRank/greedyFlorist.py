#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
	costos = sorted(c, reverse=True)

	total = 0
	factorMultiply = 0
	for a in range(0, len(costos)):
		total += costos[a] * (factorMultiply + 1)

		if (a+1)%k == 0:
			factorMultiply+=1

	return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
