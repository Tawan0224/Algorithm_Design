#Soe Min Min Latt
#6611938
#541

from collections import deque

class State:
    def __init__(self, r, c, step):
        self.r = r
        self.c = c
        self.step = step

def valid(maze, visited, r, c, M, N):
    if r < 0 or r >= M or c < 0 or c >= N:
        return False
    if maze[r][c] == 1:
        return False
    if visited[r][c]:
        return False
    return True

M, N = map(int, input().split())
sr, sc = map(int, input().split())
er, ec = map(int, input().split())

maze = []
for _ in range(M):
    maze.append(list(map(int, input().split())))

visited = [[False]*N for _ in range(M)]

q = deque()
q.append(State(sr, sc, 0))
visited[sr][sc] = True

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while q:
    cur = q.popleft()

    if cur.r == er and cur.c == ec:
        print(cur.step)
        exit()

    for i in range(4):
        nr = cur.r + dr[i]
        nc = cur.c + dc[i]

        if valid(maze, visited, nr, nc, M, N):
            visited[nr][nc] = True
            q.append(State(nr, nc, cur.step + 1))

print("No path found")
