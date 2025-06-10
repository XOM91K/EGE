l = [int(x) for x in open('15.txt')]
mx = max(l)
ct = []
for x in range(len(l) - 2):
    o = 0
    if str(l[x]).count('0') == 0:
        o += 1
    if str(l[x + 1]).count('0') == 0:
        o += 1
    if str(l[x + 2]).count('0') == 0:
        o += 1
    if o >= 2:
        if mx/2 > l[x] + l[x + 1] + l[x + 2]:
            ct.append(l[x] + l[x + 1] + l[x + 2])
print(len(ct), max(ct))