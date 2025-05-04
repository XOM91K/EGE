l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    if x[0] < x[1] < x[2] < x[3] < x[4] < x[5] < x[6]:
        if (x[0] + x[-1]) / 2 > (x[1] + x[2] + x[3] + x[4] + x[5]) / 5:
            ct += 1
print(ct)
# 11, 13, 14, 15, 15, 16]