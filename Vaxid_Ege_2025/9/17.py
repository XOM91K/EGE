l = [[int(d) for d in x.split()] for x in open('17.txt')]
ct = 0
for x in l:
    x.sort()
    if x[-1] < x[0] + x[1] + x[2]:
        if len(set(x)) == 3:
            ct += 1
print(ct)