l = [int(x) for x in open('1.txt')]
sr = sum(l) // len(l)
l = sorted(l)
med = l[len(l) // 2]
ct = 0
for x in l:
    if min(sr, med) <= x <= max(sr, med):
        ct += 1
print(sr, med, ct)