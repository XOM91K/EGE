l = [[int(d) for d in g.split()] for g in open('16.txt')]
ct = 0
for x in l:
    sm_nepovt = 0
    pr_povt = 1
    if len(set(x)) < 7:
        for y in x:
            if x.count(y) > 1:
                pr_povt *= y
            if x.count(y) == 1:
                sm_nepovt += y
        if 3 * sm_nepovt <= pr_povt:
            ct += 1
print(ct)