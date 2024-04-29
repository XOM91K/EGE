l = [sorted([int(d) for d in x.split()]) for x in open('6.txt')]
ct = 0
for x in l:
    if x[0] != x[1] and len(set(x)) < 6:
        g = x
        sm_povt = 0
        for y in x:
            if x.count(y) > 1:
                sm_povt += y
        if x[0] + x[5] < sm_povt:
            ct += 1
print(ct)