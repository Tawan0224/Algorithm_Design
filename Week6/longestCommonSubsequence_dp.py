#Soe Min Min Latt
#6611938
#541

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

"""
#Recursion
def lcs_recursive(A, B, i, j):
    if i == len(A) or j == len(B):
        return 0
    if A[i] == B[j]:
        return 1 + lcs_recursive(A, B, i + 1, j + 1)

    #if A[i] <> B[j]
    return max(lcs_recursive(A, B, i + 1, j), lcs_recursive(A, B, i, j + 1))
print(lcs_recursive(A,B,0,0))
"""

"""
#Recursion + mm
memo = {}
def lcs_memo(A, B, i, j, memo):
    if i == len(A) or j == len(B):
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if A[i] ==B[j]:
        memo[(i, j)] = 1 + lcs_memo(A,B, i+1, j+1, memo)
    else:
        memo[(i,j)] = max(lcs_memo(A, B, i + 1, j, memo), lcs_memo(A, B, i, j + 1, memo))
    return memo[(i,j)]
print(lcs_memo(A, B, 0, 0, memo))
"""

#mm -> dp
dp = [[0] * (m + 1) for i in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[n][m])
