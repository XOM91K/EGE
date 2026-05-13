l = [int(x) for x in open('22.txt')]
mx1 = str(max(l))[-1]
mx = []
ct = 0
for x in range(len(l) - 2):
    otr = []
    pol = []
    if l[x] < 0:
        otr.append(l[x])
    elif l[x] > 0:
        pol.append(l[x])
    if l[x + 1] < 0:
        otr.append(l[x + 1])
    elif l[x + 1] > 0:
        pol.append(l[x + 1])
    if l[x + 2] < 0:
        otr.append(l[x + 2])
    elif l[x + 2] > 0:
        pol.append(l[x + 2])
    if abs(sum(otr)) <= sum(pol):
        if str((l[x] * l[x + 1] * l[x + 2]))[-1] == mx1:
            ct += 1
            mx.append(abs((l[x] * l[x + 1] * l[x + 2])))
print(ct, max(mx))