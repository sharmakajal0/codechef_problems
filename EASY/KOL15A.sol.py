#!/usr/bin/env python

''' module for sum of digits in an alphanumeric string'''

def Sum_Of_Digits(S):
    '''Function Definition for calculating the sum of digits in an alphanumeric string'''
    total_sum = 0
    for x in S:
        if x.isdigit() == True:
            z = int(x)
            total_sum = total_sum + z
    return total_sum
TEST_CASES = int(input())
for _ in range(TEST_CASES):
    s = input()
    print(Sum_Of_Digits(s))
