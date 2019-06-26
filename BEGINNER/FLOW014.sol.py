#!/usr/bin/env python

##
# Question URL: https://www.codechef.com/problems/FLOW014
##

for _ in range(int(input())):
    p, q, r =map(float, input().split())
    p = p > 50
    q = q < 0.7
    r = r > 5600

    if(p and q and r):
        grade = 10
    elif(p and q):
        grade = 9
    elif(q and r):
        grade = 8
    elif(p and r):
        grade = 7
    elif(p or q or r):
        grade = 6
    else:
        grade = 5
    print(grade)