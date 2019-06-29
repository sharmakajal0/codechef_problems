import sys

def gcd(x, y):
    while x != 0 and y != 0:
        z = y
        y = x % y
        x = z
    return x + y
def second_gcd(A, gcd1):
    ret = 0
    for x in A:
        if x % gcd1 != 0:
            ret = gcd(ret, x)
    if ret == 0:
        return A[-1]
    return ret

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()

    d = 1
    answer = 0
    while d * d <= A[0]:
        if A[0] % d == 0:
            answer = max(answer, d + second_gcd(A, d))
            answer = max(answer,A[0] // d + second_gcd(A, A[0] // d))
        d = d + 1
    print(answer)