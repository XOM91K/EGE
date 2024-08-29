l = [[int(d) for d in x.split()] for x in open('11.txt')]
ct = 0
for x in l:
    ch = 0
    nch = 0
    for y in range(0, 5):
        if x[y] % 2 == 0:
            ch += x[y]
        else:
            nch += x[y]
    if (len(set(x)) == 4 and nch <= ch) or (len(set(x)) != 4 and nch > ch):
        ct += 1
print(ct)