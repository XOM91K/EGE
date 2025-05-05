l = [int(x) for x in open('3.txt')]
l = sorted(l)
ct = 0
r = set()
r2 = []
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        if l[x] + l[y] == 100 and x not in r and y not in r:
            r.add(y)
            r.add(x)
            r2.append(x)
            r2.append(y)
            ct += 1
print(ct)
print(r.__sizeof__())
print(r2.__sizeof__())