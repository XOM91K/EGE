l = [sorted([int(y) for y in x.split()]) for x in open('11.txt')]
ct = 0
for x in l:
    if x[0] != x[1]:
        if len(set(x)) < 6:
            smmxmn = x[0] + x[-1]
            smpovt = 0
            for y in x:
                if x.count(y) > 1:
                    smpovt += y
            if smmxmn < smpovt:
                ct += 1
print(ct)
