#!/usr/bin/env python    
t = int(input())
for _ in range(t):
    n = int(input())
        
    l = list(map(int, input().strip().split(' ')))
    p = len(set(l))
    print(p)    