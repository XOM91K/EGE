l = [[int(d) for d in x.split()] for x in open('31.txt')]
uch = [d[0] for d in l[:199154]]
snu = sorted(l[199154:], key=lambda d: (d[1], -d[0]))
sm_money = 0
mx_mosh = []
for x in uch:
    for y in snu:
        if y[0] >= x:
            sm_money += y[1]
            mx_mosh.append(y[0])
            break
print(sm_money, max(mx_mosh))