l = [[int(d) for d in x.split()] for x in open('14.txt')]
ct = 0
for x in l:
    if sorted(set(x)) == x:
        x.sort()
        if x[0] + x[-1] <= x[1] + x[2] + x[3]:
            ct += 1
print(ct)