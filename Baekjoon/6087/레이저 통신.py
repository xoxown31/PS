from collections import deque
import sys

MAX = sys.maxsize
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

isin = lambda i, j : 0 <= i < H and 0 <= j < W
iswall = lambda i, j : board[i][j] == '*'
canmove = lambda i, j : isin(i,j) and not iswall(i,j)

W, H = map(int, input().split())
board = [[x for x in input().strip()] for _ in range(H)]
dp = [[[MAX] * 4 for _ in range(W)] for _ in range(H)]

l = []
for i in range(H):
    for j in range(W):
        if board[i][j] == 'C': l.append((i,j))

start = l[0]
end = l[1]

queue = deque()

for i in range(4):
    vi = start[0] + di[i]
    vj = start[1] + dj[i]

    if canmove(vi,vj):
        queue.append((vi,vj,i))
        dp[vi][vj][i] = 0

while queue:
    ui, uj, dir = queue.popleft()

    for i in range(4):
        vi = ui + di[i]
        vj = uj + dj[i]

        if not canmove(vi,vj): continue

        w = dp[ui][uj][dir]

        if dir in (1,3) and i in (0,2) or dir in (0,2) and i in (1,3):
           w += 1
        
        if dp[vi][vj][i] > w:
            dp[vi][vj][i] = w
            queue.append((vi,vj,i))

print(min(dp[end[0]][end[1]]))