#Program to locate song "UNCLE JOHNY"
for _ in range(int(input())):
    n = int(input())
    list = [int(x) for x in input().split()]
    johny = list[int(input())-1]
    k = sorted(list[:n])
    print(k.index(johny)+1)
