#!/usr/bin/env python
''' solving problems from code 1 to N'''

TEST_CASES = int(input())

for _ in range(TEST_CASES):
    N, A, B, K = map(int, input().split())
    APPY_QUE = 0
    CHEF_QUE = 0

    for i in range(N):
        if i % A == 0 and i % B == 0:
            APPY_QUE += 0
            CHEF_QUE += 0

        elif i % A == 0 and i % B != 0:
            APPY_QUE += 1

        elif i % B == 0 and i % A != 0:
            CHEF_QUE += 1

    M = int(APPY_QUE + CHEF_QUE)

    if M >= K:
        print("Win")
    else:
        print("Lose")
