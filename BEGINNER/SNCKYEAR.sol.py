#!/usr/bin/env python

##
# Question URL: https://www.codechef.com/problems/SNCKYEAR
##

for _ in range(int(input())):
    N = int(input())
    if N == 2010 or N == 2015 or N == 2016 or N == 2017 or N == 2019:
        print("HOSTED")
    else:
        print("NOT HOSTED")
        