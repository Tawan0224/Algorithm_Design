#Soe Min Min Latt
#6611938
#541

import sys
sys.setrecursionlimit(10000)

''' Step3
n = int(input("Enter n: "))
x = [0] * n 

def comb(i):
    if i == n:
        print(*x)
        return 1 
    x[i] = 0
    count0 = comb(i + 1) 
    x[i] = 1
    count1 = comb(i + 1)
    return count0 + count1 

total = comb(0)
print("Total combinations:", total)
'''


''' Step4
n = int(input("Enter n: "))
k = int(input("Enter k: "))
x = [0] * n

def comb(i, s=0):
    if i == n:
        if s == k:
            print(*x)
            return 1
        else:
            return 0
    x[i] = 0
    count0 = comb(i + 1, s)
    x[i] = 1
    count1 = comb(i + 1, s + 1)
    return count0 + count1

total = comb(0)
print(f"Combinations with exactly {k} ones:", total)
'''


#Step5
n = int(input("Enter n: "))
x = [0] * n

def comb3(i):
    if i == n:
        print(*x)
        return 1
    total = 0
    for val in [0, 1, 2]:
        x[i] = val
        total += comb3(i + 1)
    return total

total = comb3(0)
print("Total combinations with 3 choices per item:", total)
