l = [int(x) for x in open('3.txt')]
ct = 0
mx = 0
mn_7 = 10 ** 10
for x in l:
    if str(x)[-1] == '7':
        mn_7 = min(mn_7, x)
for x in range(len(l) - 1):
    if (str(l[x])[-1] == '7' and str(l[x + 1])[-1] != '7') or (str(l[x])[-1] != '7' and str(l[x + 1])[-1] == '7'):
        if l[x] ** 2 + l[x + 1] ** 2 < mn_7 ** 2:
            ct += 1
            mx = max(mx, l[x] ** 2 + l[x + 1] ** 2)
print(ct, mx)