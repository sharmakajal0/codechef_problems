for _ in range(int(input())):
    n = int(input())
    S = [int(i)for i in input().split()]
    y = [None]*(n-1)
    t = S.sort()
    for x in range(n-1):
        y[x]= S[x+1]-S[x]
    print(min[y])
