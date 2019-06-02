# program for factorial
for i in range(int(input())):
    n= int(input())
    count = 0
    a=5
    while(n/a>=1):
        count += int(n/a)
        a *= 5
    print count 
