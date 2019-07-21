#!/usr/bin/env python

'''module for finding mean'''

def mean(test_array):

    '''Finding mean of a list'''
    n_length = len(test_array)
    total_sum = 0
    for i in test_array:
        total_sum = total_sum + i
    total_mean = total_sum/n_length
    if total_mean in test_array:
        print(test_array.index(total_mean) + 1)
    else:
        print('Impossible')

for _ in range(int(input())):
    N = int(input())
    TEST_LIST = list(map(int, input().split()))
    mean(TEST_LIST)
