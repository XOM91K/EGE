l = [int(x) for x in open('2.txt')]
mx_3 = 0
ct = 0
mx = 0
for x in l:
    if str(x)[-1] == '3':
        mx_3 = max(mx_3, x)
print(mx_3)
for x in range(len(l) - 1):
    if (str(l[x])[-1] == '3' and str(l[x + 1])[-1] != '3') or (str(l[x])[-1] != '3' and str(l[x + 1])[-1] == '3'):
        if l[x] ** 2 + l[x + 1] ** 2 >= mx_3 ** 2:
            ct += 1
            mx = max(mx, l[x] ** 2 + l[x + 1] ** 2)
print(ct, mx)
