# program to add two numbers
#!/usr/bin/env python
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    sum = a+b
    print(sum)
