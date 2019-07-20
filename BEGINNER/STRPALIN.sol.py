#!/usr/bin/env python

'''module for palindrome strings'''

def palindrome_substring(s_1, s_2):

    '''Function definition for palindrome substrings'''
    if s_1 & s_2:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    set_one = set(input())
    set_two = set(input())
    palindrome_substring(set_one, set_two)
    