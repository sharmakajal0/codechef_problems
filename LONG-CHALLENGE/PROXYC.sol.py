#!/usr/bin/env python
import string
import random
for _ in range(int(input())):
    D = int(input())
    P = 0
    proxy = 0
    S = input() 
    for i in range(len(S)):
        if(S[i] == 'P'):
            P += 1
    A = P/D
    if A >= 0.75:
        print(proxy)
    else:
        for d in range(D):
            if d == 1 and d == 2 and d == D - 1 and d == D - 2:
                proxy += 0

            elif d == 'P' and d + 1 =='P':
                proxy += 1
            else:
                proxy += 0
                continue
        #    else:
         #       proxy = proxy + 1
          #      break
        P = P + proxy
        A = P / D
        if A >= 0.75:
            print(proxy)
        else:
            print("-1")