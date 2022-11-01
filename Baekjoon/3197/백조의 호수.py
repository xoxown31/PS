from collections import deque
import sys

input = sys.stdin.readline

dij = [(0,1),(1,0),(0,-1),(-1,0)]

R, C = map(int, input().split())

board = [[x for x in input().strip()] for _ in range(R)]
root = [[(i,j) for j in range(C)] for i in range(R)]
rank = [[0 for _ in range(C)] for _ in range(R)]
visit = [[False for _ in range(C)] for _ in range(R)]

def isin(i, j):
    return 0 <= i < R and 0 <= j < C

def find(u):
    ui, uj = u[0], u[1]
    if u == root[ui][uj]: return u
    
    root[ui][uj] = find(root[ui][uj])
    return root[ui][uj]

def union(u1, u2):
    r1, r2 = find(u1), find(u2)

    if rank[r1[0]][r1[1]] > rank[r2[0]][r2[1]]:
        root[r2[0]][r2[1]] = r1
    elif rank[r1[0]][r1[1]] < rank[r2[0]][r2[1]]:
        root[r1[0]][r1[1]] = r2
    else:
        root[r2[0]][r2[1]] = r1
        rank[r1[0]][r1[1]] += 1

swan = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'L':
            swan.append((i,j))
            board[i][j] = '.'
            if len(swan) == 2: break

melt = deque()

for i in range(R):
    for j in range(C):
        if visit[i][j] or board[i][j] == 'X': continue
        q = deque()
        q.append((i,j))
        visit[i][j] = 1
        while q:
            ui, uj = q.popleft()
            root[ui][uj] = (i,j)
            for di, dj in dij:
                vi = ui + di
                vj = uj + dj
                if not isin(vi,vj) or visit[vi][vj]: continue
                visit[vi][vj] = True
                if board[vi][vj] == '.':
                    q.append((vi,vj))
                else:
                    melt.append((vi,vj))

res = 0
while find(swan[0]) != find(swan[1]):
    t = deque()
    while melt:
        ui, uj = melt.popleft()
        board[ui][uj] = '.'
        merge = []
        for di, dj in dij:
            vi = ui + di
            vj = uj + dj
            if not isin(vi,vj): continue
            if not visit[vi][vj] and board[vi][vj] == 'X':
                visit[vi][vj] = 1
                t.append((vi,vj))
            elif board[vi][vj] == '.':
                merge.append((vi,vj))
        for x in merge:
            if find(x) != find((ui,uj)):
                union(x, (ui,uj))
    melt = t
    res += 1

print(res)