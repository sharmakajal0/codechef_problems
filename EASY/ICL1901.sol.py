#!/usr/bin/env python

'''Module for A Weird Device'''

##
# Question URL: https://www.codechef.com/problems/ICL1901
##


def weird_device(num_one):

    '''Function definition for weird device'''
    multiply_num = num_one * 1001
    num_one = str(multiply_num)
    num_one = set(num_one)
    string_length = len(num_one)
    print(string_length ** 3)

for _ in range(int(input())):
    NUM_ONE, NUM_TWO = map(int, input().split())
    weird_device(NUM_ONE)
