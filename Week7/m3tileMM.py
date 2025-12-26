#Soe Min Min Latt
#6611938
#541

import sys
import time
sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())
memo = {}

def nWays(d,s):
    if (d,s) in memo:
        return memo[(d,s)]
    if d == L:
        if s == FLAT:
            return 1
        else:
            return 0
    else:
        counter = 0
        if s == FLAT:
            if d < L-1:
                counter += nWays(d+2, FLAT)
            counter += nWays(d+1, UPPER2)
            counter += nWays(d+1, LOWER2)
        else:
            counter += nWays(d+1, FLAT)
            if d < L-1:
                counter += nWays(d+2, s)

    memo[(d, s)] = counter
    return counter

start = time.process_time()
print(nWays(0,FLAT))
end = time.process_time()

print("running_time = ", end-start)