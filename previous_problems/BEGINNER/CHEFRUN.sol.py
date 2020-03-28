#!/usr/bin/env python

'''Module for Time'''
def time(x_one, x_two, x_three, v_one, v_two):

    '''Function Definition for Calculating time'''
    t_one = (x_three - x_one)/v_one
    t_two = (x_two - x_three)/v_two

    if t_one > t_two:
        print("Kefa")
    if t_one < t_two:
        print("Chef")
    if t_one == t_two:
        print("Draw")

for i in range(int(input())):
    x1, x2, x3, v1, v2 = map(int, input().split())
    time(x1, x2, x3, v1, v2)
