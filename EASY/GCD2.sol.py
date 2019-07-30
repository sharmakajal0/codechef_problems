#!/usr/bin/env python

'''Module for GCD 2'''

##
# Question URL: https://www.codechef.com/problems/GCD2
##

def gcd(num_one, num_two):

    '''Function definition to find the greatest common divisor'''
    if num_two == 0:
        return num_one
    return gcd(num_two, num_one % num_two)

for i in range(int(input())):
    A, B = map(int, input().split(' '))
    print(gcd(A, B))
