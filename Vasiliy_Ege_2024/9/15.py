l = [sorted([int(d) for d in x.split()]) for x in open('15.txt')]
ct = 0
for x in l:
    k = 0
    if len(set(x)) == 4:
        if x[0] == x[1] == x[2] or x[1] == x[2] == x[3] or x[2] == x[3] == x[4] or x[3] == x[4] == x[5]:
            k += 1

    if (x[0] + x[5])**2 > (x[1]**2 + x[2]**2 + x[3]**2 + x[4]**2):
        k += 1
    if k >= 1:
        ct += 1
print(ct)