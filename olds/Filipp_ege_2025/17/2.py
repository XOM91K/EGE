l = [int(x) for x in open('2.txt')]
sr = [x for x in l if str(x)[-3:] == '151']
sr = sum(sr) / len(sr)
mn = []
ct = 0
for x in range(len(l) - 2):
    ch = [len(str(abs(y))) for y in [l[x], l[x + 1], l[x + 2]]]
    if 1 <= ch.count(4) <= 2:
        kr7 = [y for y in [l[x], l[x + 1], l[x + 2]] if y % 7 == 0]
        kr13 = [y for y in [l[x], l[x + 1], l[x + 2]] if y % 13 == 0]
        if len(kr13) > len(kr7):
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                ct += 1
                mn.append(l[x] + l[x + 1] + l[x + 2])
print(ct, min(mn))