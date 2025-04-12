l = [[int(d) for d in x.split()] for x in open('13.txt')]
l = sorted(l, key=lambda d: (-(d[1] + d[2] + d[3] + d[4]), -d[-1], d[0]))
n = 1076
last_id = l[:n][::-1]
sum_last = sum(l[:n][-1][1:])
for x in last_id:
    if sum(x[1:]) > sum_last:
        print(x[0])
        break
print(len([x for x in l if sum(x[1:]) == sum_last]))
# 1. Убывание суммы набранных баллов (80, 80, 80)
# 2. Баллы за собеседование
# 3. по меньшему ID
#for x in l:
#    print(x)