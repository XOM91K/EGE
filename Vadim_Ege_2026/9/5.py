l = [[int(d) for d in x.split()] for x in open("5.txt")]
ct = 0
for x in l:
    x.sort()
    if len(set(x)) == 5:
        if (x[0] + x[-1]) / 2 == x[2] == (x[1] + x[-2]) / 2:
            ct += 1
print(ct)