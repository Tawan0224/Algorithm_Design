#Soe Min Min Latt
#6611938
#541

import time
FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())

dp = [[0]*3 for _ in range(L+2)]

dp[L][FLAT] = 1
dp[L][UPPER2] = 0
dp[L][LOWER2] = 0

for d in range(L-1, -1, -1):
    dp[d][FLAT] = dp[d+1][UPPER2] + dp[d+1][LOWER2]
    if d < L-1:
        dp[d][FLAT] += dp[d+2][FLAT]

    dp[d][UPPER2] = dp[d+1][FLAT]
    if d < L-1:
        dp[d][UPPER2] += dp[d+2][UPPER2]

    dp[d][LOWER2] = dp[d+1][FLAT]
    if d < L-1:
        dp[d][LOWER2] += dp[d+2][LOWER2]

start = time.process_time()
print(dp[0][FLAT])
end = time.process_time()

print("running_time = ", end-start)
