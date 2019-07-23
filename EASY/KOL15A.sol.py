#!/usr/bin/env python

''' module for sum of digits in an alphanumeric string'''

def sum_digits(s_array):

    '''Function Definition for calculating the sum of digits in an alphanumeric string'''
    total_sum = 0
    for i in s_array:
        if i.isdigit() is True:
            z_num = int(i)
            total_sum = total_sum + z_num
    return total_sum

TEST_CASES = int(input())
for _ in range(TEST_CASES):
    s = input()
    print(sum_digits(s))
