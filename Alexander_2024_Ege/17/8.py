l = [int(x) for x in open('8.txt')]
mx_19 = max([x for x in l if x % 100 == 19])
ct = 0
mx = 0
for x in range(len(l) - 2):
    if ((len(str(l[x])) == 4) + (len(str(l[x + 1])) == 4) + (len(str(l[x + 2])) == 4)) == 2:
        if l[x] % 3 == 0 or l[x + 1] % 3 == 0 or l[x + 2] % 3 == 0:
             if (l[x] + l[x + 1] + l[x + 2]) > mx_19:
                 ct += 1
                 mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)