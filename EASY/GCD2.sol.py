def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for i in range(int(input())):
    A, B = map(int, input().split(' '))
    print(gcd(A, B))
