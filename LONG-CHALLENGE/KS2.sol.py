#!/usr/bin/env python

'''Module for guddu on a date'''
##
# Question URL: https://www.codechef.com/problems/KS2
##

def guddu_date(int_n):

    '''Function for guddu on a date'''
    if int_n == 0:
        return 0
    return int_n % 10 + guddu_date(int(int_n/10))

for _ in range(int(input())):
    N = int(input())
    total_sum = guddu_date(N)
    total_sum = total_sum % 10
    req_ans = 10 - total_sum
    if req_ans == 10:
        req_ans = 0
    print(int(str(N) + str(req_ans)))
