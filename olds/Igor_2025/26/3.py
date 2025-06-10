l = sorted([int(x) for x in open('3.txt')])
md = l[len(l) // 2]
sr = sum(l) / len(l)
print(sr, md)
ct = 0
for x in l:
    if min(sr, md) <= x <= max(sr, md):
        ct += 1
print(ct)