l = [int(x) for x in open('22.txt')]
mn_sm = 10 ** 10
nm = 0
ln = len(l)

sm_r = [0] * ln
sm_l = [0] * ln
for i in range(0, 1): #O(1)
    smr = 0
    sml = 0
    for j in range(ln):
        if abs(j - i) <= ln // 2:
            smr += abs(j - i) * l[j]
        else:
            sml += (ln - abs(j - i)) * l[j]
    sm_r[i] = smr
    sm_l[i] = sml
l = l * 3
pr = [0] * (len(l) + 1)
for x in range(len(l)):
    pr[x + 1] = pr[x] + l[x]
print(l)
print(pr)
for i in range(ln + 1, 2 * ln):
    sm_r[i - ln] = sm_r[i - ln - 1] - l[i] + (l[i + (ln // 2)] * (ln // 2)) - (pr[i + (ln // 2)] - pr[i + 1])
    sm_l[i - ln] = sm_l[i - ln - 1] + (pr[i] - pr[i - (ln // 2 - 1)]) - (l[i - ln // 2] * (ln // 2 - 1))
mx_sm = 10 ** 10
punkt = 0
for x in range(len(sm_r)):
    if sm_r[x] + sm_l[x] < mx_sm:
        mx_sm = sm_r[x] + sm_l[x]
        punkt = x + 1
print(punkt, mx_sm)