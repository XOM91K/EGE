l = [int(x) for x in open('5.txt')]
chisla_151 = [y for y in l if str(y)[-3:] == '151']
sr_151 = sum(chisla_151) / len(chisla_151)
ct = 0
mn_sum = 10 ** 10
for x in range(len(l) - 2):
    lens = [len(str(abs(y))) for y in [l[x], l[x + 1], l[x + 2]]]
    if 1 <= lens.count(4) <= 2:
        kr7 = [1 for y in [l[x], l[x + 1], l[x + 2]] if y % 7 == 0]
        kr13 = [1 for y in [l[x], l[x + 1], l[x + 2]] if y % 13 == 0]
        if len(kr13) > len(kr7):
            if l[x] > sr_151 and l[x + 1] > sr_151 and l[x + 2] > sr_151:
                ct += 1
                mn_sum = min(mn_sum, l[x] + l[x + 1] + l[x + 2])
print(mn_sum, ct)