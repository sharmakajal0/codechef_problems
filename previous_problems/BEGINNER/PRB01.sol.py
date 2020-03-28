#!usr/bin/env python
t = int(input())
for _ in range(t):
    n = int(input())
    def isPrime(n):  
        if n <= 1: 
            return False 
        for i in range(2, n): 
            if n % i == 0: 
                return False; 
        return True 
    print("Yes") if isPrime(n) else print("No")