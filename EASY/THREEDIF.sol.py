#!/usr/bin/env python

'''Module for Three Different numbers'''

##
# Question URL: https://www.codechef.com/problems/THREEDIF
##


def three_diff(test_list):

    '''Function for three different numbers'''
    test_list.sort()
    result = (test_list[0] * (test_list[1] - 1) * (test_list[2] - 2)) % 1000000007
    return result


for _ in range(int(input())):
    TEST_LIST = list(map(int, input().split()))
    print(three_diff(TEST_LIST))
