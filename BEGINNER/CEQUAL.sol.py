#!/usr/bin/env python

'''module for finding equal pairs'''

def equal_pair(test_list, test_num):
    if len(test_list) == test_num:
        print('No')
    else:
        print('Yes')

for _ in range(int(input())):
    TEST_NUM = int(input())
    TEST_LIST = set(map(int, input().split()))
    equal_pair(TEST_LIST, TEST_NUM)
