l = [[int(d) for d in x.split()] for x in open('12.txt')]
ct = 0
for x in l:
    x = sorted(x)
    a = (x[0] + x[1] + x[2] + x[3] + x[4]) / 5
    if (x[-1] != x[-2]) and (len(set(x))) < 6 and (x[-1] > a * 3):
        ct += 1
print(ct)