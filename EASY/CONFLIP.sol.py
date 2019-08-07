#!/usr/bin/env python

'''Module for coin flip'''

##
# Question URL: https://www.codechef.com/problems/CONFLIP
##


TEST_CASES = int(input())
while TEST_CASES > 0:
    TEST_CASES -= 1
    NUM_GAMES = int(input())
    for _ in range(NUM_GAMES):
        I, N, Q = map(int, input().split())

        if N % 2 == 0 or I == Q:
            print(int(N/2))
        else:
            print(int(N/2 + 1))
