#Soe Min Min Latt
#6611938
#541

N = int(input())
prices = list(map(int, input().split()))

#brute-force
"""
def f(i):
    if i >= N:
        return 0

    # buy 1
    best = prices[i] + f(i + 1)

    # buy 2
    if i + 1 < N:
        cost2 = prices[i] + prices[i+1] - min(prices[i], prices[i+1]) * 0.5
        best = min(best, cost2 + f(i + 2))

    # buy 3
    if i + 2 < N:
        cheapest = min(prices[i], prices[i+1], prices[i+2])
        cost3 = prices[i] + prices[i+1] + prices[i+2] - cheapest
        best = min(best, cost3 + f(i + 3))

    return best
print(f"{f(0):.1f}")
"""

#memo
"""
memo = {}
def f(i):
    if i >= N:
        return 0

    if i in memo:
        return memo[i]

    best = prices[i] + f(i + 1)

    if i + 1 < N:
        cost2 = prices[i] + prices[i+1] - min(prices[i], prices[i+1]) * 0.5
        best = min(best, cost2 + f(i + 2))

    if i + 2 < N:
        cheapest = min(prices[i], prices[i+1], prices[i+2])
        cost3 = prices[i] + prices[i+1] + prices[i+2] - cheapest
        best = min(best, cost3 + f(i + 3))

    memo[i] = best
    return best
print(f"{f(0):.1f}")
"""

#dp
dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    # buy 1
    dp[i] = dp[i-1] + prices[i-1]

    # buy 2
    if i >= 2:
        dp[i] = min(
            dp[i],
            dp[i-2] + prices[i-1] + prices[i-2]
            - min(prices[i-1], prices[i-2]) * 0.5
        )

    # buy 3
    if i >= 3:
        dp[i] = min(
            dp[i],
            dp[i-3] + prices[i-1] + prices[i-2] + prices[i-3]
            - min(prices[i-1], prices[i-2], prices[i-3])
        )

print(f"{dp[N]:.1f}")




