#!/usr/bin/env python

'''module for Easy Fibonacci'''

def fibonacci_series(N):
    '''function for fibonacci series'''
    series = [0, 1]

    for i in range(2, N):
        series.append(series[i - 1] + series[i - 2])
    
    return series

def altered_fibonacci_series(series):
    '''function for altering fibonacci series'''
    return list(map(lambda f: f % 10, series))

def pick_even_position(source_list):
    '''function for picking even position from list'''
    return [value for index, value in enumerate(source_list) if index % 2 != 0]


def final_subsequence(source_list):

    '''function for final subsequence'''
    while(len(source_list) > 1):
        source_list = pick_even_position(source_list)
    return source_list

for _ in range(int(input())):
    N = int(input())
    series = fibonacci_series(N)
    D = altered_fibonacci_series(series)

    print(*final_subsequence(D))
