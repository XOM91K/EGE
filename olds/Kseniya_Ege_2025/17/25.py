l = [int(x) for x in open('25.txt')]
mx7 = len([x for x in l if str(x)[-1] == '3'and len(str(abs(x))) == 4])
sm = []
for x in range(len(l) - 2):
    sp = sorted([l[x], l[x + 1], l[x + 2]])
    if sp[-1] + sp[-2] > mx7 ** 2:
        sm.append(l[x] + l[x +1 ] + l[x + 2])
print(len(sm), abs(max(sm)))