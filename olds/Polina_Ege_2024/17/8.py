l = [int(x) for x in open('8.txt')]
mn_37 = 10 ** 10
mx_73 = 0
mn = 10 ** 10
ct = 0

for x in l:
    if x % 37 == 0:
        mn_37 = min(mn_37, x)
    if x % 73 == 0:
        mx_73 = max(mx_73, x)
for x in range(len(l) - 1):
    if (438 < l[x] < 518 and not(438 < l[x + 1] < 518)) or (438 < l[x + 1] < 518 and not(438 < l[x] < 518)):
        ct += 1
        mn = min(mn, l[x] + l[x + 1])
print(ct, mn)