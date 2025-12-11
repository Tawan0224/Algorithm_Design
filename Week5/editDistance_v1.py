#Soe Min Min Latt
#6611938
#541
import time
A = input("Enter first string: ")
B = input("Enter second string: ")

def editDistance_v1(A, B, i = 0, j = 0):
    if (i == len(A)):
        return len(B)-j
    if (j == len(B)):
        return len(A)-i
    if (A[i] == B[j]):
        return editDistance_v1(A, B, i + 1, j + 1)

    substitute = (1 + editDistance_v1(A, B, i + 1, j + 1))
    insert = (1 + editDistance_v1(A, B, i, j + 1))
    delete = (1 + editDistance_v1(A, B, i + 1, j))

    return min(substitute, insert, delete)
start = time.process_time()
print(editDistance_v1(A, B))
finish = time.process_time()
print ("running_time = ", finish-start)