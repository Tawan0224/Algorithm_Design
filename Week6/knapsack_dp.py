#Soe Min Min Latt
#6611938
#541

import sys
sys.setrecursionlimit(10000)

N,M = map(int, input().split())
v = [0] * N
w = [0] * N
for i in range(N):
    v[i], w[i] = map(int, input().split())

dp = [[0] * (M + 1) for i in range(N + 1)]

for i in range(N-1, -1, -1):
    for C in range (M+1):
        skip = dp[i +1][C]
        take = 0
        if w[i] <= C:
            take = v[i] + dp[i + 1] [C - w[i]]
        dp[i][C] = max(skip, take)
print(dp[0][M])
