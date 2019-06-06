#!usr/bin/env python
n, k = map(int, input().split())
total = 0
for i in range(n):
    t = int(input())
    if (t % k == 0):
        total = total + 1
print(total)