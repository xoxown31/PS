from collections import deque
import sys

input = sys.stdin.readline
dij = [(1,0),(-1,0),(0,1),(0,-1)]

R, C = map(int, input().split())

cave = [[x for x in input().strip()] for _ in range(R)]

N = int(input())
heights = [int(x) for x in input().split()]

def throw(h, i):
    if i%2 == 0:
        i = 0
        while i < C:
            if cave[h][i] == 'x':
                cave[h][i] = '.'
                break
            i += 1
    else:
        i = C-1
        while i >= 0:
            if cave[h][i] == 'x':
                cave[h][i] = '.'
                break
            i -= 1

def getFloatingCluster():
    visited = [[0] * C for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if cave[i][j] == 'x' and visited[i][j] == 0:
                visited[i][j] = 1
                cluster = [(i,j)]
                root = R-i
                isFloat = 1
                queue = deque()
                queue.append((i,j))
                while queue:
                    ui, uj = queue.popleft()

                    for di, dj in dij:
                        vi, vj = ui + di, uj + dj
                        if 0 <= vi < R and 0 <= vj < C:
                            if cave[vi][vj] == 'x' and visited[vi][vj] == 0:
                                visited[vi][vj] = 1
                                root = R-vi
                                cluster.append((vi,vj))
                                queue.append((vi,vj))
                        if root == 1:
                            isFloat = 0
                if isFloat == 1:
                    return cluster
    if isFloat == 0:
        return []

def dropCluster(cluster):
    for i, j in sorted(cluster, reverse = True):
        cave[i][j] = '.'
        cave[i+1][j] = 'x'
    
    for i in range(len(cluster)):
        cluster[i] = (cluster[i][0]+1, cluster[i][1])

    for i, j in cluster:
        if i == R-1 or (i+1,j) not in cluster and cave[i+1][j] == 'x':
            return
    
    dropCluster(cluster)

def printCave():
    for i in range(R):
        print(*cave[i],sep='')

for i in range(N):
    throw(R-heights[i], i)
    l = getFloatingCluster()
    if l:
        dropCluster(l)

printCave()