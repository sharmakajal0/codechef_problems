#!/usr/bin/env python

'''Module for matching strings'''

def match(count_n, s_1, s_2):

    '''Function Definition to match two strings'''
    count_a, count_b = 0, 0
    for i in range(count_n):
        if s_1[i] == '1':
            count_a += 1
        if s_2[i] == '1':
            count_b += 1
    print('YES' if count_a == count_b else 'NO')

for _ in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()
    match(n, s1, s2)
