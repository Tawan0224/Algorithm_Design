#Soe Min Min Latt
#6611938
#541

class obj:
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.r = v / w

x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()
item = []
for i in range(N):
    item.append(obj(int(w[i]), int(v[i])))

def getKey(x):
    return x.r

item.sort(key=getKey, reverse=True)

maxV = 0
count = 0

def Bound(i, C):
    global item, N
    sw = 0
    sv = 0
    j = i
    f = 1.0
    while j < N and f == 1.0:
        wj = min(C - sw, item[j].w)
        f = float(wj) / item[j].w
        sw += f * item[j].w
        sv += f * item[j].v
        j += 1
    return sv

def dfs(i, sumW, sumV):
    global maxV, item, N, M, count
    count += 1

    if i == N:
        maxV = max(maxV, sumV)
        return

    remainingCapacity = M - sumW

    if item[i].w <= remainingCapacity:
        bound_take = sumV + item[i].v + Bound(i + 1, remainingCapacity - item[i].w)
        bound_skip = sumV + Bound(i + 1, remainingCapacity)

        if bound_take >= bound_skip:
            if bound_take > maxV:
                dfs(i + 1, sumW + item[i].w, sumV + item[i].v)
            if bound_skip > maxV:
                dfs(i + 1, sumW, sumV)
        else:
            if bound_skip > maxV:
                dfs(i + 1, sumW, sumV)
            if bound_take > maxV:
                dfs(i + 1, sumW + item[i].w, sumV + item[i].v)
    else:
        bound_skip = sumV + Bound(i + 1, remainingCapacity)
        if bound_skip > maxV:
            dfs(i + 1, sumW, sumV)

dfs(0, 0, 0)
print(maxV)
print("Recursive call counts:", count)