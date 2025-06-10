l = [int(x) for x in open('1.txt')]
l = sorted(l)
med = l[len(l) // 2]
sr = sum(l) // len(l)
ct = 0
for x in l:
    if min(med, sr) <= x <= max(med, sr):
        ct += 1
print(ct)