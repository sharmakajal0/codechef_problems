#!/usr/bin/env python
L = int(input())
B = int(input())
perimeter = 2 * (L + B)
area = L * B
if perimeter == area:
    print("Eq")
    print(perimeter)
elif perimeter < area:
    print("Area")
    print(area)
else:
    print("Peri")
    print(perimeter)