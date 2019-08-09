#!/usr/bin/env python

'''Module for walk on axis'''

def walk_onaxis(num_bulb):

    '''Function for walk on axis'''
    items_difference = num_bulb - (num_bulb - 1)
    ans = 0
    ans += num_bulb
    ans += num_bulb
    ans += items_difference * ((num_bulb * (num_bulb - 1))/ 2)
    return ans

if __name__ == "__main__":
    for _ in range(int(input())):
        TEST_INTEGER = int(input())
        print(int(walk_onaxis(TEST_INTEGER)))
