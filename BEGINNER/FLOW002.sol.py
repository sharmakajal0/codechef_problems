# Program to find remainder
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    num = (a%b)
    print(num)
