#статград февраль 2025
s = [[int(d) for d in x.split()] for x in open(r'C:\Users\Zarif\Desktop\26.txt')][1:]
s = sorted(s)
sl = {}
for x in s:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
ct_max = 0
rez = 0
for x in sl:
    sl[x] = sorted(set(sl[x]))
    ct = 0
    for i in range(len(sl[x]) - 2):
        if abs(sl[x][i + 1] - sl[x][i]) > 1000 or abs(sl[x][i + 1] - sl[x][i + 2]) > 1000:
            ct += 1
    if len(sl[x]) >= 2:
        if abs(sl[x][1] - sl[x][0]) > 1000:
            ct += 1
        if abs(sl[x][-1] - sl[x][-2]) > 1000:
            ct += 1
    if ct >= ct_max:
        ct_max = ct
        rez = x
print(ct_max, rez)
print(sl[58612])