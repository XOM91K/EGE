l = [[int(d) for d in x.split()] for x in open('14.txt')]
l = sorted(l, key=lambda d: d[1])
lc = []
time_opened = 0
mx_rzn = 0
for x in l:
    if x[0] >= time_opened:
        if len(lc) % 3 == 0 and x[0] - time_opened >= 10 and len(lc) > 0:
            print('Уборка! Внимание!', x[0] - time_opened)
            time_opened = x[1]

            lc.append(x)
        elif len(lc) % 3 != 0 or len(lc) == 0:
            time_opened = x[1]
            lc.append(x)
print(lc)
print(len(lc))
print(mx_rzn)
for x in l:
    if x[0] > 1246:
        print(x)
#  [1246, 1259], [1264, 1273]