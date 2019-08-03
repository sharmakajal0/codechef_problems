#!/usr/bin/env python

'''Module for splitting candies'''

##
# Question URL: https://www.codechef.com/problems/SPCANDY/
##

def split_candy(total_candies, student_count):

    '''Function Definition for splitting candies'''
    if student_count == 0:
        print(0, total_candies)
    else:
        split = int(total_candies/student_count)
        remaining = total_candies % student_count
        print(split, remaining)

for _ in range(int(input())):
    N, K = map(int, input().split())
    split_candy(N, K)
