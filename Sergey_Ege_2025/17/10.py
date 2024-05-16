l = [int(x) for x in open('10.txt')]
mx8 = 0
ct = 0
mn = 10 ** 10
for x in l:
    if str(abs(x))[0] == '8':
        mx8 = max(mx8, x)
for x in range(len(l) - 2):
    k = 0
    if str(abs(l[x]))[0] == '6':
        k += 1
    if str(abs(l[x + 1]))[0] == '6':
        k += 1
    if str(abs(l[x + 2]))[0] == '6':
        k += 1
    if k <= 1 and (l[x] + l[x + 1] + l[x + 2]) >= mx8:
        ct += 1
        mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)
