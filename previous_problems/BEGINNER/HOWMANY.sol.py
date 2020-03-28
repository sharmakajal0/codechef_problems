#!/usr/bin/env python

'''module for Finding number of digits'''

def num_digits(n_one):

    '''Function Definition for finding Number of digits'''
    if len(n_one) > 3:
        print("More than 3 digits")
    else:
        print(len(n_one))

TEST_NUMBER = input()
num_digits(TEST_NUMBER)
