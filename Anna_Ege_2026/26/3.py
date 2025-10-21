l = [int(x) for x in open('3.txt')]
l.sort()
inds = []
ct = 0
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        if l[x] + l[y] == 100 and x not in inds and y not in inds:
            inds.append(x)
            inds.append(y)
            ct += 1
print(l)
print(ct)