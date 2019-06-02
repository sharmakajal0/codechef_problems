t = int(input())
def fours(n):
    count = 0
    while(n>0):
        if(n%10)==4:
            count = count + 1
        n = n//10
    return(count)
for _ in range(t):
    n = int(input())
    print(fours(n))
