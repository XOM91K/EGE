l = sorted([int(x) for x in open('13.txt')])
mn_mass = 1
for x in l:
    if x <= mn_mass:
        mn_mass += x
    else:
        break
ct = 0
for x in l:
    if x > mn_mass:
        ct += 1
print(mn_mass, ct)