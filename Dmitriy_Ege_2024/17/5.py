l = [int(x) for x in open('5.txt')]
mx_5 = max([x for x in l if str(x)[-1] == '5'])
ct = 0
mn = 10**10
for x in range(len(l) - 1):
    if (str(l[x])[-1] == '8' and str(l[x + 1])[-1] != '8') or (str(l[x])[-1] != '8' and str(l[x + 1])[-1] == '8'):
        if l[x] ** 2 + l[x + 1] ** 2 > mx_5 ** 2:
            ct += 1
            mn = min(mn, l[x] ** 2 + l[x + 1] ** 2)
print(ct, mn)