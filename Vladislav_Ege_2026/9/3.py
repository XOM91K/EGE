l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    nepovt = [d for d in x if x.count(d) == 1]
    if len(nepovt) == 6:
        x.sort()
        if (x[-1] + x[0]) / 2 < (x[1] + x[2] + x[3] + x[4]) / 4:
            ct += 1
print(ct)