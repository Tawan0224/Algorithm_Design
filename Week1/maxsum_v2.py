#Soe Min Min Latt
#6611938
#541

import time
start = time.process_time()

def accumulated(x): #Find how to calculate prefix sum from "https://www.geeksforgeeks.org/dsa/prefix-sum-array-implementation-applications-competitive-programming/"
    accu = [0] * len(x) #Fill a new list with zeros
    accu[0] = x[0] #Just copy the first element
    for i in range(1, len(x)):
        accu[i] = accu[i-1] + x[i]
    return accu

def Sum(acc, i, j): #Used Calude to learn why acc[j] - acc[i-1] gives the sum from index i to j.
    if i == 0: #Just return the value from index j
        return acc[j]
    else:
        return acc[j] - acc[i-1]  #sum(i to j)

def accumulation(x):
    n = len(x)
    accu = accumulated(x)
    max_Sum = 0
    for i in range(n):
        for j in range(i, n):
            current_Sum = Sum(accu, i, j)
            if current_Sum > max_Sum:
                max_Sum = current_Sum
    return max_Sum


arr = list(map(int, input().split()))
result = accumulation(arr)

finish = time.process_time()

print(f"Maximum subsequence sum: {result}")
print("running_time =", finish - start)
