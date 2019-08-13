#!/usr/bin/env python

'''Module for sum and GCD'''

##
# Question URL: https://www.codechef.com/problems/SUMAGCD
##

def gcd(num_one, num_two):

    '''Function for GCD'''
    while num_one != 0 and num_two != 0:
        temp_var = num_two
        num_two = num_one % num_two
        num_one = temp_var

    return num_one + num_two

def second_gcd(test_list, gcd1):

    '''Function for second GCD'''
    ret = 0

    for i in test_list:
        if i % gcd1 != 0:
            ret = gcd(ret, i)

    if ret == 0:
        return test_list[-1]

    return ret


for _ in range(int(input())):
    n = int(input())
    A_LIST = list(map(int, input().split()))
    A_LIST.sort()

    d = 1
    answer = 0

    while d * d <= A_LIST[0]:
        if A_LIST[0] % d == 0:
            answer = max(answer, d + second_gcd(A_LIST, d))
            answer = max(answer, A_LIST[0] // d + second_gcd(A_LIST, A_LIST[0] // d))

        d = d + 1

    print(answer)
