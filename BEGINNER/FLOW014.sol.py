#!/usr/bin/env python

##
# Question URL: https://www.codechef.com/problems/FLOW014
##

t = int(input())

for _ in range(t):
    p, q, r = input().split()
    p, q, r = int(p), float(q), int(r)
    p > 50
    q < 0.7
    r > 5600

    if(p and q and r):
        grade = 10
    elif(p and q):
        grade = 9
    elif(q and r):
        grade = 8
    elif(p and r):
        grade = 7
    elif(p and ( not q and not r) or q and (not p and not r) or r and (not p and not q)):
        grade = 6
    elif(not p and not q and not r):
        grade = 5
    print(grade)