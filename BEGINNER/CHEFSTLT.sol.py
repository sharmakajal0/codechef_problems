#!/usr/bin/env python
t = int(input())
for _ in range(t):
    
    S = input()
    T = input()
    c1 = 0
    c2 = 0
    for i in range(len(S)):
        if(S[i] != '?' and T[i] != '?' and S[i] != T[i]):
            c1 += 1
        elif(S[i] == '?' or T[i] == '?'):
            c2 += 1
    print(c1 , c1 + c2)