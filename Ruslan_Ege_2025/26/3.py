l = sorted([int(x) for x in open('3.txt')])[::-1]
osn = l[0]
i = 1
ct = 1
while i != len(l):
    if abs(l[i] - osn) >= 9:
        osn = l[i]
        ct += 1
    i += 1
print(ct, osn)