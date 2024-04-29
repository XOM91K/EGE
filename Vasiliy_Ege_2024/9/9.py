l = [sorted([int(d) for d in x.split()]) for x in open('12.txt')]
ct = 0
su = 0
for x in l:
    su += 1
    if len(set(x)) == 6:
        if x[0] == x[1] or x[1] == x[2] or x[2] == x[3] or x[3] == x[4] or x[4] == x[5] or x[5] == x[6] or x[6] == x[7]:
            if x[0] != x[1] or x[2] or x[3]:
                ct += 1
print(su, ct)