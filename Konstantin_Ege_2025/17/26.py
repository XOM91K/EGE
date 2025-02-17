l=[int(x) for x in open('26.txt')]
ct=0
mn_ch = min([x for x in l if x % 3 == 0])
mx_ch = max([x for x in l if x % 10 == 3])
s = []
for x in range(len(l) - 1):
    ai = 0
    if l[x] >= mn_ch:
        if l[x] <= mx_ch:
            ai += 1
    if l[x + 1] >= mn_ch:
        if l[x + 1] <= mx_ch:
            ai += 1
    if ai == 1:
        ct += 1
        s.append((l[x] ** 2) + (l[x + 1] ** 2))
print(ct, min(s))