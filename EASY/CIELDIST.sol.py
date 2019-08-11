#!/usr/bin/env python

'''Module for Minimum Distance'''

##
# Question URL: https://www.codechef.com/problems/CIELDIST
##

def distance(d_s, d_t, total_distance):

    '''Function definition for minimum distance'''
    ans1, ans2, ans3, ans4 = 0, 0, 0, 0
    if d_s + d_t < total_distance:
        ans1 = total_distance - d_s - d_t

    elif d_s >= total_distance + d_t:
        ans3 = d_s - total_distance - d_t

    elif d_t >= total_distance + d_s:
        ans4 = d_t - total_distance - d_s

    ans = max(0, ans1, ans2, ans3, ans4)

    print(ans)


for _ in range(int(input())):
    ds, dt, d = map(float, input().split())
    distance(ds, dt, d)
