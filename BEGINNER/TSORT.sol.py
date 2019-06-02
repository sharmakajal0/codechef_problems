t = int(input())
l = []
while t:
    a = int(input())
    l.append(a)
    t = t-1
l.sort()
for x in l:
    print(x)

