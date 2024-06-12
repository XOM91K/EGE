l = [int(x) for x in open('6.txt')]
sr = []
ct = 0
mn = 10 ** 10
for x in l:
    if abs(x) % 1000 == 151:
        sr.append(x)
sr = sum(sr) / len(sr)
for x in range(len(l) - 2):
    g = [len(str(abs(l[x]))), len(str(abs(l[x + 1]))), len(str(abs(l[x + 2])))]
    if 1 <= g.count(4) <= 2:
        ct13 = len([d for d in [l[x], l[x + 1], l[x + 2]] if d % 13 == 0])
        ct7 = len([d for d in [l[x], l[x + 1], l[x + 2]] if d % 7 == 0])
        if ct13 > ct7:
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                ct += 1
                mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)