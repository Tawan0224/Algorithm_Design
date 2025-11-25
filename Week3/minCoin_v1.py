#Soe Min Min Latt
#6611938
#541
import time
import sys
coins = list(map(int, input().split()))
amount = int(input())
sys.setrecursionlimit(10000)

def mincoin_v1(n, C):
    count = 0
    count += 1

    if n == 0:
        return 0
    if n < 0:
        return float('inf')
    v = float('inf')

    for c in C:
        v = min(mincoin_v1(n - c, C) + 1, v)
    return v
start = time.process_time()
result = mincoin_v1(amount, coins)
finish = time.process_time()

print(result)
print("running_time = ", finish-start)
