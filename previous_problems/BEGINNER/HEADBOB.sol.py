#!/usr/bin/env python

'''Module for Identification'''

def identity_indian(test_string):

    '''Function definition to identify an Indian'''
    if 'I' in test_string:
        print("INDIAN")
    elif 'Y' in test_string:
        print("NOT INDIAN")
    else:
        print("NOT SURE")


for _ in range(int(input())):
    n = int(input())
    test_subject = input()
    identity_indian(test_subject)
