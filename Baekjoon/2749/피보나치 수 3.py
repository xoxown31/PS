n = int(input())
p = 1000000

def mul(l1, l2):
    l = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            l[i][j] = (l1[i][0] * l2[0][j] + l1[i][1] * l2[1][j]) % p
    
    return l

if n <= 1:
    print(n)
else:
    l = [[1,0],[0,1]]
    t = [[1,1],[1,0]]
    while n > 0:
        if n%2:
            l = mul(l,t)
        t = mul(t,t)
        n //= 2
    print(l[0][1])