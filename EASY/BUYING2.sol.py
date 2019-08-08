#!/usr/bin/env python

'''Module for buying sweets'''

def buying(sweet_price, my_list):

    '''Function for buying sweets'''
    total_sum = sum(my_list)
    max_count = 101
    for i in my_list:
        if i < max_count:
            max_count = i
    if max_count < total_sum % sweet_price:
        print('-1')
    else:
        print(total_sum // sweet_price)

TEST_CASES = int(input())
for _ in range(TEST_CASES):
    N, X = map(int, input().split())
    TEST_LIST = list(map(int, input().split()))
    buying(X, TEST_LIST)
