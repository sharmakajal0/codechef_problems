#!/usr/bin/env python

'''Module for pretty numbers'''

##
# Question URL: https://www.codechef.com/problems/NUM239
##

def pretty_numbers(range_one, range_two):

    '''Function Definition to count the pretty numbers in the given range'''
    count = 0
    for i in range(range_one, range_two + 1):
        if i % 10 == 2 or i % 10 == 3 or i % 10 == 9:
            count += 1
        else:
            continue
    return count

for _ in range(int(input())):
    RANGE_ONE, RANGE_TWO = map(int, input().split())
    print(pretty_numbers(RANGE_ONE, RANGE_TWO))
