a = -1
l = []
while a != 0:
    a = int(input())
    if a != 0:
        l.append(a)
l = sorted(l)
print(l[-1] + l[-2])
print(l[0] + l[1])