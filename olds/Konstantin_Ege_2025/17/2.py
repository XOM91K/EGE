l = [int(x) for x in open('2.txt')]
ct = 0
r = []
for x in range(len(l) - 1):
    if (l[x] % 3 == 0 or l[x + 1] % 3 == 0) and (l[x] + l[x + 1]) % 5 == 0:
        ct += 1
        r.append(l[x] + l[x + 1])
print(ct)
print(max(r))