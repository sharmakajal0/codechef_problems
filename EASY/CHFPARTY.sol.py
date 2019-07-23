#!/usr/bin/env python

'''Module for Chef and Party'''

def join(total_friends, a_i):

    '''Function Definition for the friends who will join the party given the conditions'''
    a_i = sorted(a_i)
    total_count = 0
    for i in range(total_friends):
        if a_i[i] <= total_count:
            total_count += 1
        else:
            break
    return total_count

for _ in range(int(input())):
    INT_N = int(input())
    TEST_ARRAY = list(map(int, input().split()))
    print(join(INT_N, TEST_ARRAY))
