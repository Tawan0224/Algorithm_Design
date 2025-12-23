#Soe Min Min Latt
#6611938
#541

N = int(input())
colors = [tuple(map(int, input().split())) for _ in range(N)]
dp = []

memo = {}
def ulti_grey(i, vivid, dull, used):
    color = (i, vivid, dull, used)
    if color in memo:
        return memo[color]

    if i == N:
        if used:
            return abs(vivid - dull)
        else:
            return float('inf')

    skip = ulti_grey(i + 1, vivid, dull, used)
    v, d = colors[i]
    take = ulti_grey(i + 1, vivid * v, dull + d, True)

    memo[color] = min(skip, take)
    return memo[color]

print(ulti_grey(0, 1, 0, False))