l = sorted([int(x) for x in open('1.txt')])
med = l[len(l) // 2]
sr = sum(l) / len(l)
ct = 0
mn = min(sr, med)
mx = max(sr, med)
for x in l:
    if mn <= x <= mx:
        ct += 1
print(ct)