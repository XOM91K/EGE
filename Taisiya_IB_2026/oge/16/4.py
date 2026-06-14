d = 1
l = []
while d != 0:
    d = int(input())
    if d == 0:
        break
    l.append(d)
l = sorted(l)
print(l[-1] + l[-2])
print(l[0] + l[1])