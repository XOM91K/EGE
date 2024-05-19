l = [int(x) for x in open('22.txt')]
mn_sm = 10 ** 10
nm = 0
ln = len(l)
sm_r = [0] * ln
sm_l = [0] * ln
for i in range(0, 1):
    smr = 0
    sml = 0
    for j in range(ln):
        if abs(j - i) <= ln // 2:
            smr += abs(j - i) * l[j]
        else:
            sml += (ln - abs(j - i)) * l[j]
    sm_r[i] = smr
    sm_l[i] = sml
print(sm_r)
print(sm_l)