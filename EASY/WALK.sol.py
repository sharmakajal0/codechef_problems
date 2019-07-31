#!/usr/bin/env python

'''Module for walk'''

##
# Question URL: https://www.codechef.com/problems/WALK
##

def walk(test_list):

    '''Function Definition for walk'''
    count = 0
    for i, value in list(enumerate(test_list)):
        if (value + i) > count:
            count = value + i
    return count

for _ in range(int(input())):
    N = int(input())
    my_list = list(map(int, input().split()))
    print(walk(my_list))
