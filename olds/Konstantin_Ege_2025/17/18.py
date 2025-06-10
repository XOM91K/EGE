l = [int(x) for x in open('18.txt')]
ct=0
qq = 0
mn = 10 ** 10
mn_ch = ([x for x in l if abs(x) % 100 == 28])
qq = sum(mn_ch) / len(mn_ch)
for x in range(len(l) - 2):
    ct4 = 0
    if len(str(abs(l[x]))) == 4:
        ct4 += 1
    if len(str(abs(l[x + 1]))) == 4:
        ct4 += 1
    if len(str(abs(l[x + 2]))) == 4:
        ct4 += 1
    if ct4 >= 1:
        ct5 = 0
        if abs(l[x]) % 100 == 11:
            ct5 += 1
        if abs(l[x + 1]) % 100 == 11:
            ct5 += 1
        if abs(l[x + 2]) % 100 == 11:
            ct5 += 1
        if ct5 == 2:
            ct6 = 0
            if l[x] > qq:
                ct6 += 1
            if l[x + 1] > qq:
                ct6 += 1
            if l[x + 2] > qq:
                ct6 += 1
            if ct6 == 3:
                ct += 1
                mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)