#!usr/bin/env python
x, y = map(float, input().split())
x = float(x)
y = float(y)
if(x % 5 == 0) and (y >(x + 0.50)):
    print(y-(x+0.5))
else:
    print(y)