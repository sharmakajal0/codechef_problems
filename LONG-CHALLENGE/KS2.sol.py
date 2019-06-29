#!/usr/bin/env python

##
# Question URL: https://www.codechef.com/problems/KS2
##

def sum(n):
    if n == 0:
        return 0
    return (n % 10 + sum(int(n/10)))

t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    s = sum(n)
    s = s % 10
    ans = 10 - s
    if ans == 10:
        ans = 0
    print(int(str(n) + str(ans)))

