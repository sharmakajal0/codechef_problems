#!/usr/bin/env python

'''Module for magic pairs'''

##
# Question URL: https://www.codechef.com/problems/ALEXNUMB
##

def alex_numbers(int_num):

    '''Function definition for alex numbers'''
    count = int_num * (int_num - 1) // 2
    print(count)

for i in range(int(input())):
    N = int(input())
    TEST_ARRAY = input()
    alex_numbers(N)
