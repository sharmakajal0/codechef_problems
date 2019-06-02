t = int(input())
for _ in range(t):
    n = int(input())
    if(360%n)==0:
        print("y", end=" ")
    else:
        print("n", end= " ")
    if n<=360:
        print("y", end=" ")
    else:
        print("n", end= " ")
    if 360 >= n*(n+1)/2:
        print("y")
    else:
        print("n")
