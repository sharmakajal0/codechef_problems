#!/usr/bin/env python


def time(x1, x2, x3, v1, v2):
    t1 = (x3 - x1)/v1
    t2 = (x2 - x3)/v2

    if t1 > t2:
        print("Kefa")
    if t1 < t2:
        print("Chef")
    if t1 == t2:
        print("Draw")

for i in range(int(input())):
    x1, x2, x3, v1, v2 = map(int, input().split())
    time(x1, x2, x3, v1, v2)