#Soe Min Min Latt
#6611938
#541

def merge_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, lc = merge_count(arr[:mid])
    right, rc = merge_count(arr[mid:])
    merged = []
    count = lc + rc
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count

def read_input():
    while True:
        line = input().strip()
        if line != "":
            return int(line)

t = read_input()

for _ in range(t):
    n = read_input()
    arr = []
    for __ in range(n):
        arr.append(read_input())

    _, count = merge_count(arr)
    print(count)