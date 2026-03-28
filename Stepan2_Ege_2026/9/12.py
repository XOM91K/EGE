l = [[int(d) for d in x.split()] for x in open('12.txt')]
ct = 0
for x in l:
    x = sorted(x)
    if x.count(x[5]) == 1:
        povt2 = [d for d in x if x.count(d) > 1]
        if len(povt2) >= 1:
            if x[5] / 3 > (x[0] + x[1] + x[2] + x[3] + x[4]) / 5:
                ct += 1
print(ct)