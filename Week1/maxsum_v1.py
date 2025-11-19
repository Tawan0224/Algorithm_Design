#Soe Min Min Latt
#6611938
#541

import time
start = time.process_time()


def Sum (x, i, j):
    s = 0
    for k in range (i, j+1):
        s += x[k]
    return s

def straightforward(x):
    n = len(x)
    max_Sum = 0
    for i in range(n):
        for j in range(i,n):
            current_Sum = Sum(x, i, j)
            if current_Sum > max_Sum:
                max_Sum = current_Sum
    return max_Sum

#arr = [-2, -3, 4, -1, -2, 1, 5, -3]
#print(straightforward(arr))

arr = list(map(int, input().split()))
result = straightforward(arr)

finish = time.process_time()

print(f"Maximum subsequence sum: {result}")
print("running_time = ", finish-start)