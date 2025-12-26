#Soe Min Min Latt
#6611938
#541

n = int(input())
cost = list(map(int, input().split()))

if n == 0:
    print(0)

if n == 1:
    print(cost[0])

dp = [0] * n
dp[0] = cost[0]
dp[1] = cost[1]

for i in range(2, n):
    dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

print(dp[n - 1])

