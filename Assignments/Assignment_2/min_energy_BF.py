#Soe Min Min Latt
#6611938
#541

n = int(input())
cost = list(map(int, input().split()))


def min_energy_BF(cost, i):
    n = len(cost)
    if i >= n:
        return 0

    return cost[i] + min(
        min_energy_BF(cost, i + 1),
        min_energy_BF(cost, i + 2)
    )


result = min_energy_BF(cost, -1)
print(result)