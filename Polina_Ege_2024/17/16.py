l = [int(x) for x in open('16.txt')]
mx_3 = 10 ** 7
ct = 0
mx = -10 ** 7
for x in l:
    if str(abs(x))[0] == '5':
        mx_3 = min(mx_3, x)
for x in range(len(l) - 1):
    if (str(abs(l[x]))[-1] == '4' and str(abs(l[x + 1]))[-1] != '4') or (str(abs(l[x]))[-1] != '4' and str(abs(l[x + 1]))[-1] == '4'):
        if (l[x] + l[x + 1]) % mx_3 != 0:
            ct += 1
            mx = max(mx, l[x] + l[x + 1])
print(ct, mx)