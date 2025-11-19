#Soe Min Min Latt
#6611938
#541

import time
start = time.process_time()

def kadane(arr): #Used GPT to understand Kadane's algorithm
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i]) #Start a NEW subsequence from current element, EXTEND the existing subsequence
        max_sum = max(max_sum, current_sum)
    return max_sum

arr = list(map(int, input().split()))
result = kadane(arr)

finish = time.process_time()

print(f"Maximum subsequence sum: {result}")
print("running_time =", finish - start)
