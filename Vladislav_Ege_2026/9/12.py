l = [[int(d) for d in x.split()] for x in open('12.txt')]
ct = 0
for x in l:
    if x == sorted(set(x)):
        x.sort()
        if x[0] + x[-1] <= x[1] + x[2] + x[3]:
            ct += 1
print(ct)

