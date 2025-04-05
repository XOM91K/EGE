l = [int(x) for x in open('2.txt')]
l = sorted(l)[::-1]
ct_corjs = 1
osn = l[0]
for x in range(1, len(l)):
    if osn - l[x] >= 8:
        osn = l[x]
        ct_corjs += 1
print(ct_corjs, osn)