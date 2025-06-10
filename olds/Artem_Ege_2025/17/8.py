l = [int(x) for x in open('8.txt')]
sr151 = [x for x in l if str(x)[-3:] == '151']
sr151 = sum(sr151) / len(sr151)
mn = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4:
        k += 1
    if len(str(abs(l[x + 2]))) == 4:
        k += 1
    if 1 <= k <= 2:
        k7 = 0
        k13 = 0
        if l[x] % 13 == 0:
            k13 += 1
        if l[x] % 7 == 0:
            k7 += 1
        if l[x + 1] % 13 == 0:
            k13 += 1
        if l[x + 1] % 7 == 0:
            k7 += 1
        if l[x + 2] % 13 == 0:
            k13 += 1
        if l[x + 2] % 7 == 0:
            k7 += 1
        if k13 > k7:
            if l[x] > sr151 and l[x + 1] > sr151 and l[x + 2] > sr151:
                mn.append(l[x] + l[x + 1] + l[x + 2])
print(len(mn), min(mn))
