#!/usr/bin/env python

t = int(input())
while (t):
    t -= 1
    d = int(input())
    s = input()
    p = 0
    proxy = 0

    for i in range(d):
        if(s[i] == 'P'):
            p += 1
    A = (p * 100)/d
    
    if (A < 75):
        for i in range(2, d-2):
            if s[i] == "A" and s[i - 1] == 'P' and s[i - 2] == 'P' and s[i + 1] == 'P' and s[i + 2] == 'P': 
                p += 1
                proxy += 1
                A = (p * 100)/d
                if (A >= 75):
                    print(proxy)
                    break
        if A >= 75:
            print(proxy)
        else:
            print("-1")
    else:
        print("0")