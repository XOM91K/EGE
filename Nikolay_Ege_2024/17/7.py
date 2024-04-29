l = [int(x) for x in open('7.txt')]
sr = 0
su = 0
ct = 0
col = 0
mx = 0
for x in l:
    if len(str(x)) > 1 and str(x)[-1] == str(x)[-2]:
        su += x
        ct += 1
sr = su / ct
for x in range(len(l) - 1):
    if (len(str(l[x + 1])) > 1 and str(l[x])[-1] == str(l[x + 1])[-2]) or (len(str(l[x])) > 1 and str(l[x])[-2] == str(l[x + 1])[-1]):
        if (l[x] % 11 == 0 and l[x + 1] % 11 != 0) or (l[x] % 11 != 0 and l[x + 1] % 11 == 0):
            if (l[x] ** 2 + l[x + 1] ** 2) >= sr ** 2:
                col += 1
                mx = max(mx, (l[x] ** 2 + l[x + 1] ** 2))
print(col, mx)