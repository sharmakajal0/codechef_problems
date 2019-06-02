#!/usr/bin/env python
#program for subtraction of two numbers
a, b = map(int, input().split(" "))

a -= b

if (a % 10) == 9:
    print(a - 1)
else:
    print(a + 1)

