#!/usr/bin/env python

'''Module for Chef and Notebooks'''

##
# Question URL: https://www.codechef.com/problems/CNOTE
##

for _ in range(int(input())):
    X, Y, K, N = map(int, input().split())
    for i in range(N):
        P, C = map(int, input().split())
        if P >= X - Y and C <= K:
            count += 1
    if count > 0:
        print("luckychef")

    else:
        print("UnluckyChef")
