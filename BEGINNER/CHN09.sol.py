#!/usr/bin/env python

for _ in range(int(input())):
    s = str(input())
    amber = 0
    brass = 0
    for i in s:
        if i == 'a':
            amber += 1
        elif i == 'b':
            brass += 1
    if amber > brass:
        print(brass)
    elif brass > amber:
        print(amber)
    else:
        print(amber)