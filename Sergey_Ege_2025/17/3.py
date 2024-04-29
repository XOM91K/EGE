l = [int(d) for d in open('3.txt')]
mn_37 = 10 ** 10
mx_73 = -10 ** 9
for x in l:
    if x % 37 == 0:
        mn_37 = min(mn_37, x)
    if x % 73 == 0:
        mx_73 = max(mx_73, x)
ct = 0
mn = 10 ** 10
for x in range(len(l) - 1):
    k = 0
    if mx_73 <= l[x] <= mn_37:
        k += 1
    if mx_73 <= l[x + 1] <= mn_37:
        k += 1
    if k == 1:
        ct += 1
        mn = min(mn, l[x] + l[x + 1])
print(ct, mn)