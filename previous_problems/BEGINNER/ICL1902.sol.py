import math
t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    while(n != 0):    
        y = int(math.sqrt(n))
        count += 1
        n = n - (y * y)
    print(count)