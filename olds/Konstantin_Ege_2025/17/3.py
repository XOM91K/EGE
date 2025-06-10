l = [int(x) for x in open('3.txt')]
sr = []
for x in l:
    if x % 2 != 0:
        sr.append(x)
sr = sum(sr) / len(sr)
ct = 0
r = []
for x in range(len(l) - 1):
    if (l[x] % 5 == 0 and l[x + 1] < sr) or (l[x] < sr and l[x + 1] % 5 == 0):
        ct += 1
        r.append(l[x] + l[x + 1])
print(ct, max(r))