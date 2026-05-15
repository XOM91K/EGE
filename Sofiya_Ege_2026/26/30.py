l = [[int(d) for d in g.split()] for g in open('30.txt')]
l = sorted(l, key=lambda d: d[0])
banks = []

for x in range(20):
    banks.append([0, 0])
# banks[0].append(5)
# print(banks)
times_max = 0
for x in l:
    for y in range(len(banks)):
        if x[0] >= banks[y][-1]:
            if banks[y][-1] == 0:
                banks[y].append(x[1] + x[0])
                break
            times_max = max(times_max, banks[y][-1] - x[0])
            start = x[0]
            banks[y][0] = start
            banks[y].append(start + x[1])
            break
    else:
        mn_time = 10000
        ind_bank = 10000
        for z in range(len(banks)):
            if banks[z][-1] <= mn_time:
                mn_time = banks[z][-1]
        for z in range(len(banks)):
            if mn_time == banks[z][-1]:
                ind_bank = min(ind_bank, z)
        times_max = max(times_max, banks[ind_bank][-1] - x[0])
        start = banks[ind_bank][-1]
        banks[ind_bank][0] = start
        banks[ind_bank].append(start + x[1])

print(times_max)
print(max(banks, key=len)[0])
# 663 1432 ответ в задании, откуда я его взял (офф. ответ)
# 1454  2449 мой ответ учителя (который выдает этот код)
# 1454 2449  ответ ученика, который пишет ЕГЭ на 100 баллов и умный