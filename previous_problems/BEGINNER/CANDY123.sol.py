#!/usr/bin/env python

##
# Question URL: https://www.codechef.com/problems/CANDY123
##

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    i = 1
    while(True):
        if i%2==0:
            b = b - i
            if b < 0:
                print("Limak")
                break
        else:
            a = a - i
            if a < 0:
                print("Bob")
                break
        i = i + 1