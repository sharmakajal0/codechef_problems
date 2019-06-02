t = int(input())
def sumOfDigits(n):
    return 0 if n == 0 else int(n%10)+sumOfDigits(int(n/10))
for _ in range(t):
    n = int(input())
    print(sumOfDigits(n))
