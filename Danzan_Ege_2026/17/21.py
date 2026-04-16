l = [int(x) for x in open('21.txt')]
mx37 = max([d for d in l if str(d)[-2:] == '37'])
ct = 0
sm = 0
for x in range(len(l) - 3):
    k = 0
    if l[x] > mx37:
        k += 1
    if l[x + 1] > mx37:
        k += 1
    if l[x + 2] > mx37:
        k += 1
    if l[x + 3] > mx37:
        k += 1
    if k == 2:
        q = 0
        ch = []
        if str(l[x])[-1] == str(l[x])[-2]:
            q += 1
            ch.append(l[x])
        if str(l[x + 1])[-1] == str(l[x + 1])[-2]:
            q += 1
            ch.append(l[x + 1])
        if str(l[x + 2])[-1] == str(l[x + 2])[-2]:
            q += 1
            ch.append(l[x + 2])
        if str(l[x + 3])[-1] == str(l[x + 3])[-2]:
            q += 1
            ch.append(l[x + 3])
        if q == 1:
            ct += 1
            sm += sum(ch)
print(ct, sm)

