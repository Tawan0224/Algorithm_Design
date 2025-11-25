#Soe Min Min Latt
#6611938
#541
import time
import sys
coins = list(map(int, input().split()))
amount = int(input())
sys.setrecursionlimit(10000)
minCoin = {}

def mincoin_v2(n, C):
    if n in minCoin:
        return minCoin[n]
    if n == 0:
        return 0
    if n < 0:
        return float('inf')

    v = float('inf')
    for c in C:
        v = min(v, mincoin_v2(n - c, C) + 1)

    minCoin[n] = v
    return v
start = time.process_time()
result = mincoin_v2(amount, coins)
finish = time.process_time()

print(result)
print("running_time = ", finish-start)
