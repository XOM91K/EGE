l = [sorted([int(d) for d in x.split()]) for x in open('5.txt')]
ct = 0
k = 0
for x in l:
    if len(set(x)) == 2 and list(set(x))[0] + list(set(x))[1] == 180:
            ct += 1
    if x[0] == 90 and x[1] == 90 and x[2] == 90 and x[3] == 90:
        ct += 1
print(ct)