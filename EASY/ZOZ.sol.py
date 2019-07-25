#!/usr/bin/env python

'''Module for valid position'''

##
# Question URL: https://www.codechef.com/problems/ZOZ
##


def valid_position(test_array, test_num):

    '''Function definition for searching the valid number of positions in a list'''
    count = 0
    total_sum = sum(test_array)

    for i in test_array:
        if i + test_num > total_sum - i:
            count += 1
    return count

for _ in range(int(input())):
    N, K = map(int, input().split())
    NUM = list(map(int, input().split()))
    print(valid_position(NUM, K))
