#Soe Min Min Latt
#6611938
#541

import time
import sys

coins = list(map(int, input().split()))
V = int(input())
sys.setrecursionlimit(10000)

def mincoin_DP(coins, V):
    mm = [10**12] * (V + 1)
    mm[0] = 0

    for v in range(1, V + 1):
        for c in coins:
            if c <= v:
                mm[v] = min(mm[v], 1 + mm[v - c])
    return mm[V]

start = time.process_time()
result = mincoin_DP(coins, V)
finish = time.process_time()

print(result)
print("running_time = ", finish - start)

