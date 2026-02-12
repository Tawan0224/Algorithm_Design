#Soe Min Min Latt
#6611938
#541

# Straightforward Exponentiation
#runnint time: O(x)
a, x = map(int, input().split())
modulo = 2147483647

def exponentiation_sf(a, x):
    result = 1
    for i in range(x):
        result = result * a
    return result % modulo
print(exponentiation_sf(a, x))