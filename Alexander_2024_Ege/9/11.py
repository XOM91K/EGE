l = [[int(d) for d in x.split()] for x in open('11.txt')]
stb = [[d[x] for d in l] for x in range(6)]
ct_str = 0
for x in l:
    ct = 0
    for y in range(len(x)):
        if x.count(x[y]) == 1 and stb[y].count(x[y]) < 170:
            ct += 1
    if 1 <= ct <= 4:
        ct_str += 1
print(ct_str)