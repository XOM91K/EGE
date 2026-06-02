n = 199154
uch = [int(x) for x in open('17.txt').readlines()[:n]]
sn = [[int(d) for d in x.split()] for x in open('17.txt').readlines()[n:]]
print(uch)
sn = sorted(sn, key=lambda d: (d[1], -d[0]))
# Требуется определить общую стоимость закупки
# и максимальную мощность снегоуборщика, входящего в число купленных.
sm = 0
mx_mosh = 0
for x in uch:
    for y in sn:
        if x <= y[0]:
            sm += y[1]
            mx_mosh = max(mx_mosh, y[0])
            break
print(sm, mx_mosh)