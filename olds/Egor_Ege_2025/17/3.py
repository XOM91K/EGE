l = [int(x) for x in open('3.txt')]
sr151 = [x for x in l if str(x)[-3:] == '151']
sr151 = sum(sr151) / len(sr151)
ct = 0
mn = 10 ** 10
for x in range(len(l) - 2):
    ch = [len(str(abs(y))) for y in [l[x], l[x + 1], l[x + 2]]]
    if 1 <= ch.count(4) <= 2:
        kr13 = [y for y in [l[x], l[x + 1], l[x + 2]] if y % 13 == 0]
        kr7 = [y for y in [l[x], l[x + 1], l[x + 2]] if y % 7 == 0]
        if len(kr13) > len(kr7):
            if l[x] > sr151 and l[x + 1] > sr151 and l[x + 2] > sr151:
                ct += 1
                mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)