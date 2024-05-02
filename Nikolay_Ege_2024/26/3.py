D = 5000
E = 1500
l = sorted([int(x) for x in open('3.txt')])
d_D = []
d_E = []
for x in l:
    if x <= 500 and sum(d_E) + x <= E:
        d_E.append(x)
    elif x > 500 and sum(d_D) + x <= D:
        d_D.append(x)
DD = []
EE = []
for x in range(len(l) - 1, -1, -1):
    if E - sum(d_E) + d_E[-1] >= l[x] and l[x] <= 500:
        EE.append(l[x])
    if D - sum(d_D) + d_D[-1] >= l[x] and l[x] > 500:
        DD.append(l[x])
print(DD, EE)
print(len(d_E) + len(d_D), max(DD) + max(EE))