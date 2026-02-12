#Soe Min Min Latt
#6611938
#541

# divide and conquer Exponentiation
# time complexity: O(log x)
a, x = map(int, input().split())
modulo = 2147483647
def exponentiation_dc(a, x):
    if x == 0:
        return 1

    if x % 2 == 0:
        result = (exponentiation_dc(a, x // 2) * exponentiation_dc(a, x // 2))
    else:
        result = a * exponentiation_dc(a, x // 2 * exponentiation_dc(a, x // 2))
    return result % modulo
print(exponentiation_dc(a, x))