#Soe Min Min Latt
#6611938
#541

values = list(map(int, input().split()))
n = len(values)

def search(i, assign):
    if i == n:
        sumA = 0
        sumB = 0
        for j in range(n):
            if assign[j] == 0:
                sumA += values[j]
            else:
                sumB += values[j]
        return abs(sumA - sumB)

    assign[i] = 0
    diffA = search(i + 1, assign)

    assign[i] = 1
    diffB = search(i + 1, assign)

    return min(diffA, diffB)

assign = [0] * n
result = search(0, assign)
print(result)