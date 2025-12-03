#Soe Min Min Latt
#6611938
#541

import time
import sys

sys.setrecursionlimit(10000)
N,M = map(int,input("Number_of_items(N) Max_capacity(M): ").split())
w = list(map(int, input("weight_0 weight_1 . . . weight_N-1: ").split()))
v = list(map(int,input("value_0  value_1  . . . value_N-1: ").split()))

x = [0]*N
count_v1 = 0
def comb(i):
    global count_v1
    count_v1 += 1
    if i == N:
        sw = sv = 0
        for j in range(N):
            if x[j] == 1:
                sw += w[j]
                sv += v[j]

        if sw > M:
            return -1
        else:
            return sv
    else:
        x[i] = 0
        a = comb(i+1)
        x[i] = 1
        b = comb(i+1)
        return max(a,b)
start = time.process_time()
print(comb(0))
finish = time.process_time()
print ("running_time = ", finish-start)
print(f"Number of recursive calls: {count_v1}")

