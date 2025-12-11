#Soe Min Min Latt
#6611938
#541

import sys
import time
sys.setrecursionlimit(10000)
A = input("Enter first string: ")
B = input("Enter second string: ")
memo = {}
def editDistance_v2(A, B, i, j, memo):
    if (i, j) in memo:
        return memo[(i, j)]

    if i == len(A):
        return len(B) - j
    if j == len(B):
        return len(A) - i

    if A[i] == B[j]:
        memo[(i, j)] = editDistance_v2(A, B, i + 1, j + 1, memo)
        return memo[(i, j)]

    insert  = 1 + editDistance_v2(A, B, i, j + 1, memo)
    delete  = 1 + editDistance_v2(A, B, i + 1, j, memo)
    substitute = 1 + editDistance_v2(A, B, i + 1, j + 1, memo)

    memo[(i, j)] = min(insert, delete, substitute)
    return memo[(i, j)]

start = time.process_time()
print(editDistance_v2(A, B, 0, 0, memo))
finish = time.process_time()
print ("running_time = ", finish-start)



