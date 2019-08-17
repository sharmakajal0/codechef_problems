#!/usr/bin/env python

'''Module for approximation'''

##
# Question URL: https://www.codechef.com/problems/APPROX
##

def approximation(test_integer):

    '''Function for approximation'''
    value_a, value_b = 103993, 33102
    for i in range(test_integer + 1):
        if i == 1:
            print('.', end='')
        print(value_a // value_b, end='')
        value_a = (value_a % value_b) * 10
    print('')

for _ in range(int(input())):
    K = int(input())
    approximation(K)
