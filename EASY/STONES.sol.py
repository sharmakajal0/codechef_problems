#!/usr/bin/env python

##
# Question URL: https://www.codechef.com/problems/STONES
##

t = int(input())
while(t > 0):
    m = str(input())
    n = str(input())
    count = 0
    for i in n:
        if i in m:
            count += 1
    print(count)
    t -= 1
