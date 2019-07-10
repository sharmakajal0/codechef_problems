#!/usr/bin/env python

''' module for counting total amount of dollars to be paid'''

TEST_CASES = int(input())
while TEST_CASES > 0:
    TEST_CASES -= 1
    N, K = map(int, input().split())
    TOTAL_MONEY = 0
    for i in range(N):
        T, D = map(int, input().split())
        if T < K:
            K = K - T
        else:
            TOTAL_MONEY = TOTAL_MONEY + (T - K) * D
            K = 0

    print(TOTAL_MONEY)
