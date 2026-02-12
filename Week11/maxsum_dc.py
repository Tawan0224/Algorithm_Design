#Soe Min Min Latt
#6611938
#541

A = list(map(int, input().split()))
def maxSubArraySum(A, p, r):
    # Base case
    if p == r:
        return A[p]

    q = (p + r) // 2
    return max(
        maxSubArraySum(A, p, q),        # Left half
        maxSubArraySum(A, q + 1, r),    # Right half
        maxCrossingSum(A, p, q, r)      # Crossing
    )

def maxCrossingSum(A, p, q, r):
    maxLeftSum = A[q]
    current_sum = 0
    for i in range(q, p - 1, -1): # q to p
        current_sum += A[i]
        if current_sum > maxLeftSum:
            maxLeftSum = current_sum

    maxRightSum = A[q + 1]
    current_sum = 0
    for i in range(q + 1, r + 1): # q+1 to r
        current_sum += A[i]
        if current_sum > maxRightSum:
            maxRightSum = current_sum

    return maxLeftSum + maxRightSum

print(maxSubArraySum(A, 0, len(A) - 1))

