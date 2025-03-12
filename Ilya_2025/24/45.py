import re
a = open(r'C:\Users\Zarif\Downloads\403_1 (4).txt').readline()
a = a.replace('XX', '1')
a = a.replace('YY', '2')
a = a.replace('ZZ', '3')
ct = 1
mx_ct = 1

for x in range(len(a) - 1):
    if a[x] != a[x + 1] and a[x] in '123' and a[x + 1] in '123':
        ct += 1
    else:
        mx_ct = max(mx_ct, ct)
        ct = 1
print(mx_ct * 2)