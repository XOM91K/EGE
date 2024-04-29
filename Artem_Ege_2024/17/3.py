l = [int(x) for x in open('3.txt')]
ct = 0
mx = 0
mn_68 = 10 ** 10
for x in l:
    if len(str(x)) > 1 and str(x)[-1] == '8' and str(x)[-2] == '6':
        mn_68 = min(mn_68, x)
for x in range(len(l) - 1):
    if (str(l[x])[-2:] == '68' and str(l[x + 1])[-2:] != '68') or (str(l[x])[-2:] != '68' and str(l[x + 1])[-2:] == '68'):
        if l[x] ** 2 + l[x + 1] ** 2 >= mn_68 ** 2:
            ct += 1
            mx = max(mx, l[x] ** 2 + l[x + 1] ** 2)
print(ct, mx)