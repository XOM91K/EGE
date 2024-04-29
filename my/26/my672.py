l = sorted([int(x) for x in open('my672.txt')])
D = 5000
E = 1500
D_l = []
E_l = []
for x in l:
    if x > 500 and D - sum(D_l) - x >= 0:
        D_l.append(x)
    elif x <= 500 and E - sum(E_l) - x >= 0:
        E_l.append(x)
del D_l[-1]
del E_l[-1]
l = l[::-1]
for x in l:
    if x > 500 and D - sum(D_l) - x >= 0:
        D_l.append(x)
        break
for x in l:
    if x <= 500 and E - sum(E_l) - x >= 0:
        E_l.append(x)
        break
print(D_l)
print(E_l)
print(len(D_l) + len(E_l), D_l[-1] + E_l[-1])