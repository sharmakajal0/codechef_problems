#!/usr/bin/env python
t = int(input())
for i in range(t):
    quantity, price = map(int, input().split())
    if quantity <= 1000:
        total = quantity * price
    if quantity >= 1000:
        total = quantity * price - (quantity * price)* 0.1
        
    print("%.6f"%total)