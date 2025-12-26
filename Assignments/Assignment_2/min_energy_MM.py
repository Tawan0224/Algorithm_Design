#Soe Min Min Latt
#6611938
#541

n = int(input())
cost = list(map(int, input().split()))
memo = {}

def min_energy_MM(cost, i, memo):
    n = len(cost)
    if i >= n:
        return 0
    if i in memo:
        return memo[i]

    memo[i] = cost[i] + min(
        min_energy_MM(cost, i + 1, memo),
        min_energy_MM(cost, i + 2, memo)
    )
    return memo[i]


result = min_energy_MM(cost, -1, memo)
print(result)