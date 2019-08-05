#!/usr/bin/env python

'''Module for attic crossing'''

##
# Question URL: https://www.codechef.com/problems/ATTIC
##


def attic(test_string):

    '''Function definition for attic crossing'''
    count = 0
    days = 0
    initial = 1
    # a = len(test_string)
    for _, sym in enumerate(test_string, 0):
        if sym == '.':
            count += 1
        else:
            if count >= initial:
                days += 1
                initial = count + 1
            count = 0

    return days

for _ in range(int(input())):
    TEST_STRING = input()
    print(attic(TEST_STRING))
