l = [int(x) for x in open('5.txt')]
mx_1001 = 0
for x in l:
    if abs(x) % 1001 == 0:
        mx_1001 = max(mx_1001, abs(x))
print(mx_1001)
ct = 0
mn = 10 ** 10
for x in range(len(l) - 1):
    if 100 <= abs(l[x]) <= 999 or 100 <= abs(l[x + 1]) <= 999:
        if l[x] + l[x + 1] > mx_1001:
            ct += 1
            mn = min(mn, l[x] + l[x + 1])
print(ct, mn)