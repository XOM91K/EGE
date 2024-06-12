l = [int(x) for x in open('14.txt')]
mx_rzl = 0
mx_rz = 0
ct = 0
for x in l:
    mx_rzl = max(mx_rzl, len(set(str(abs(x)))))
for x in l:
    if len(set(str(abs(x)))) == mx_rzl:
        mx_rz = max(mx_rz, x)
for x in range(len(l) - 2):
    if (abs(l[x]) ** 0.5 % 1 == 0 and abs(l[x + 1]) ** 0.5 % 1 != 0 and abs(l[x + 2]) ** 0.5 % 1 != 0) \
        or (abs(l[x]) ** 0.5 % 1 != 0 and abs(l[x + 1]) ** 0.5 % 1 == 0 and abs(l[x + 2]) ** 0.5 % 1 != 0) \
        or (abs(l[x]) ** 0.5 % 1 != 0 and abs(l[x + 1]) ** 0.5 % 1 != 0 and abs(l[x + 2]) ** 0.5 % 1 == 0):
        sm = l[x] + l[x + 1] + l[x + 2]
        if abs(l[x]) ** 0.5 % 1 == 0:
            sm -= l[x]
        elif abs(l[x + 1]) ** 0.5 % 1 == 0:
            sm -= l[x + 1]
        elif abs(l[x + 2]) ** 0.5 % 1 == 0:
            sm -= l[x + 2]
        if sm >= mx_rz:
            print(l[x], l[x + 1], l[x + 2])
            ct += 1
print(ct)