#Soe Min Min Latt
#6611938
#541
import time
prices = list(map(int, input().split()))
prices = [0] + prices
L = len(prices) - 1

def maxRev_v2(l, memo):
    if memo[l] != -1:
        return memo[l]
    if l == 0:
        return 0

    v = float('-inf')
    for i in range(1, l + 1):
        v = max(v, prices[i] + maxRev_v2(l - i, memo))

    memo[l] = v
    return v

memo = [-1] * (L + 1)
start = time.process_time()
result = maxRev_v2(L, memo)
finish = time.process_time()
print(result)
print("running_time = ", finish-start)
