a = sorted([int(i) for i in open('16.txt')])[::-1]
osn = a[0]
ct = 0
for i in range(len(a)):
    if osn - a[i] >= 9:
        osn = a[i]
        ct += 1
print(ct)
print(osn)