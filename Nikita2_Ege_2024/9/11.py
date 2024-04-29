l = [sorted([int(d) for d in x.split()]) for x in open('11.txt')]
ct = 0
for x in l:
    if len(set(x)) == 3:
        if max(x) % min(x) != 0:
            if (x[0] + x[1]) * 2 < x[2] + x[3]:
                print(x)
                ct += 1
print(ct)