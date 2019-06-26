#!/usr/bin/env python
    
##
# Question URL: https://www.codechef.com/problems/TABLET
##


t = int(input())
while(t > 0):
    n, budget = map(int, input().split())
    current_max_area = 0
    for i in range(n): 
        width, height, price = map(int, input().split())
        area = width * height
        if budget >= price and area > current_max_area:
            current_max_area = area
    t -= 1
    if current_max_area > 0:
        print(current_max_area)
    else:
        print("no tablet")
