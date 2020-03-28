#!usr/bin/env python
p1, p2, w, ml = 0, 0, 0, 0
n = int(input())
for _ in range(n):
    s, t = map(int, input().split())
    p1 += s
    p2 += t
    l = abs(p1 - p2)
    if(ml < l):
        ml = l
        if(p1 > p2):
            w = 1
        else:
            w = 2
print(str(w)+' '+str(ml))