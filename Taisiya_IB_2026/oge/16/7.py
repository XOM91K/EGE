d = 1
l = []
while d != 0:
    d = int(input())
    if d == 0:
        break
    if len(str(d)) == 2 and d % 8 == 0:
        l.append(d)
print(sum(l))