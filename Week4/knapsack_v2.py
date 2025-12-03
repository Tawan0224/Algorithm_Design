#Soe Min Min Latt
#6611938
#541

import time
import sys
sys.setrecursionlimit(10000)
N,M = map(int,input("Number_of_items(N) Max_capacity(M): ").split())
w = list(map(int, input("weight_0 weight_1 . . . weight_N-1: ").split()))
v = list(map(int,input("value_0  value_1  . . . value_N-1: ").split()))
count_v2 = 0
def maxVal(i, C):
    global count_v2
    count_v2 += 1
    if i == N:
        return 0
    else:
        skip = maxVal(i+1, C)
        if w[i] <= C:
            take = v[i] + maxVal(i+1,C-w[i])
        else:
            take = -1
        return max(skip, take)
start = time.process_time()
print(maxVal(0,M))
finish = time.process_time()
print("running_time = ", finish-start)
print(f"Number of recursive calls: {count_v2}")
