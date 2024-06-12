l = [[int(d) for d in x.split()] for x in open('8.txt')]
ct = 0
for x in l:
    nch = 0
    for y in x:
        if y % 2 != 0:
            nch += 1
    if (nch == 3 and len(set(x)) == len(x)) or (nch != 3 and len(set(x)) != len(x)):
        ct += 1
print(ct)