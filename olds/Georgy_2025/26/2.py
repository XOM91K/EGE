l = [int(x) for x in open('2.txt')]
l = sorted(set(l))[::-1]
ct = 1
mn = 0
osn = l[0]
for x in range(1, len(l)):
    if osn - l[x] >= 9:
        ct += 1
        osn = l[x]
print(ct, osn)