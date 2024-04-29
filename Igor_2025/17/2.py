l = [int(x) for x in open('2.txt')]
ct = 0
mx = 0
mx25 = max([d for d in l if abs(d) % 100 == 15])
for x in range(len(l) - 2):
    d = [len(str(l[x])), len(str(l[x + 1])), len(str(l[x + 2]))]
    if d.count(4) == 1:
        if l[x] + l[x + 1] + l[x + 2] >= mx25:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)