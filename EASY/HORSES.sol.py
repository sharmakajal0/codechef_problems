for _ in range(int(input())):
    n = int(input())
    horses = [int(i)for i in input().split()]
    y = [None]*(n-1)
    for i in range(n-1):
        t = horses.sort()
    for x in range(n-1):
        y[x]= horses[x+1]-horses[x]
    print(min(y))
