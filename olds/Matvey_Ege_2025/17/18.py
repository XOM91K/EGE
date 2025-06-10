l = [int(x) for x in open('18.txt')]
c = []
c2 = []
for i in l:
    if i % 17 == 0 and i > 0:
        c.append(i)
    if str(i)[-2:] == '69':
        c2.append(i)
c2 = max(c2)
c = sorted(c)
c = c[0] + c[1]
e = []
for x in range(len(l) - 3):
    ln = [len(str(abs(l[x]))), len(str(abs(l[x + 1]))), len(str(abs(l[x + 2]))), len(str(abs(l[x + 3])))]
    dl = [l[x] % 18, l[x + 1] % 18, l[x + 2] % 18, l[x + 3] % 18]
    if ln.count(3) == 2 and dl.count(0) == 1:
        if (l[x] + l[x + 1] + l[x + 2] + l[x + 3]) % c == 0:
            if (l[x] * l[x + 1] * l[x + 2] * l[x + 3]) <= c2 ** 2:
                e.append((l[x] + l[x + 1] + l[x + 2] + l[x + 3]) ** 2)
print(len(e), min(e))