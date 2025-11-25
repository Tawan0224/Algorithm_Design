#Soe Min Min Latt
#6611938
#541
import time
prices = list(map(int, input().split()))
prices = [0] + prices
L = len(prices) - 1

def maxRev_v1(l):
    if l == 0:
        return 0
    v = float('-inf')
    for i in range(1, l + 1):
        #Check all possible first cut lengths and update maximum revenue
        v = max(v, prices[i] + maxRev_v1(l - i))
    return v
start = time.process_time()
result = maxRev_v1(L)
finish = time.process_time()
print(result)
print("running_time = ", finish-start)