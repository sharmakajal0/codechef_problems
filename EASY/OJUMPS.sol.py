#!/usr/bin/env python

'''Module for Chef Jumping'''

##
# Question URL: https://www.codechef.com/problems/OJUMPS
##

def chef_jumping(test_num):

    '''Function Definition for chef jumping'''
    if test_num % 6 == 0 or test_num % 6 == 1 or test_num % 6 == 3:
        print("yes")
    else:
        print("no")

for _ in range(int(input())):
    TEST_NUM = int(input())
    chef_jumping(TEST_NUM)
