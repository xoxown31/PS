import sys

input = sys.stdin.readline

N, B = map(int, input().split())

l = [[int(x) for x in input().split()] for _ in range(N)]

def mul(l1, l2):
    N = len(l1)
    res = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            res[i][j] = sum([l1[i][k] * l2[k][j] for k in range(N)]) % 1000
    
    return res

def pow(a, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    l = pow(a,b//2)
    if b%2 == 0:
        return mul(l,l)
    else:
        return mul(mul(l,l),a)

res = pow(l, B)
for i in range(N):
    print(*res[i])