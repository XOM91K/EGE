l =[sorted([int(d) for d in x.split()]) for x in open('9.2')]
ct = 0
for x in l:
    if x[3] < x[0] + x[1] + x[2]:
        if x[0] == x[1] and x[0] == x[2] and x[0] == x[3]:
            if x[1] == x[2] and x[1] == x[3]:
                if x[2] == x[3]:
                    ct += 1
print(ct)