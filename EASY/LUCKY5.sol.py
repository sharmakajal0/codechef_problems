#!/usr/bin/env python

'''Module for lucky 5'''

##
# Question URL: https://www.codechef.com/problems/LUCKY5
##

def unlucky_digits(str_value):

    '''Function for Unlucky digits'''
    count = 0
    for i in str_value:
        if i != '4' and i != '7':
            count += 1

    return count

T = int(input())

for _ in range(T):
    N = input().strip()
    print(unlucky_digits(N))
