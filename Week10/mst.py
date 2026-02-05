#Soe Min Min Latt
#6611938
#541

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

        return True


def kruskal(V, edges):
    edges.sort(key=lambda x: x[2])
    dsu = DisjointSet(V)

    mst_weight = 0
    sets = V

    for u, v, w in edges:
        if dsu.union(u, v):
            mst_weight += w
            sets -= 1
            if sets == 1:
                break

    return mst_weight

V, E = map(int, input().split())
edges = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

print(kruskal(V, edges))
