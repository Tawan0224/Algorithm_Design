#Soe Min Min Latt
#6611938
#541

import copy
from collections import deque

class state():
    def __init__(self, n):
        self.a = [-1] * n
        self.b = 0

def conflict(Q, i, j):
    if Q[i] == Q[j] or abs(Q[i] - Q[j]) == abs(i - j):
        return True
    else:
        return False

def is_safe(Q, col):
    for i in range(col):
        if conflict(Q, i, col):
            return False
    return True

def print_queens(Q):
    n = len(Q)
    board = [['.'] * n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

def bfs_N_Queen(N):
    q = deque()

    start = state(N)
    q.append(start)

    while q:
        current = q.popleft()

        if current.b == N:
            return current.a

        col = current.b

        for i in range(N):
            child = copy.deepcopy(current)
            child.a[col] = i
            if is_safe(child.a, col):
                child.b += 1
                q.append(child)

    return None

if __name__ == "__main__":
    N = int(input("Enter N: "))

    solution = bfs_N_Queen(N)

    if solution:
        print("One valid solution:\n")
        print_queens(solution)
    else:
        print("No solution found.")
