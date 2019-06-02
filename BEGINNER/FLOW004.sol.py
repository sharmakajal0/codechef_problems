t = int(input())
def first(n):
    while n>=10:
        n = n/10
    return int(n)
def last(n):
    return (n%10)
for i in range(t):
    n = int(input())
    print(first(n)+last(n))
