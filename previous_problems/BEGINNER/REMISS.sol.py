#!/usr/bin/env python

##
# Question URL: https://www.codechef.com/problems/REMISS 
##

t = int(input())
try:
    for i in range(t):
        a, b = map(int, input().split())
        p = max(a, b)
        q = a + b
        print(p, q)
except(ValueError, EOFError):
    pass
