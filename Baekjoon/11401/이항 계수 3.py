N, K = map(int, input().split())

p = 1000000007

a = 1
for i in range(N, N-K, -1):
    a *= i
    a %= p

b = 1
for i in range(K):
    b *= i+1
    b %= p

def pow(n : int, r : int) -> int:
    if r <= 1:
        return n ** r % p
    if r%2 == 0:
        return pow(n,r//2) ** 2 % p
    else:
        return n * pow(n,r//2) ** 2 % p

print(a * pow(b, p-2) % p)