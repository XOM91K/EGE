l = sorted([int(x) for x in open('2.txt')])[::-1]
osn = l[0]
ct = 1
for x in l:
    if osn - x >= 9:
        ct += 1
        osn = x
print(ct, osn)