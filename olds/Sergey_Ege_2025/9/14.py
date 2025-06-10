l = [sorted([int(d) for d in x.split()]) for x in open('14.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4 and (x.count(x[2]) == 3 or x.count(x[3]) == 3):
        sm_povt = 0
        if x.count(x[2]) == 3:
            sm_povt = x[2] * 3
        else:
            sm_povt = x[3] * 3
        sm_nepovt = sum(x) - sm_povt
        if (sm_nepovt / 3) < sm_povt:
            print(x)
            ct += 1
print(ct)