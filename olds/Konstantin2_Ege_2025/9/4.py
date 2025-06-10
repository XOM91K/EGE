l = [[int(d) for d in x.split()] for x in open('4.txt')]
k = 0
sm = 0
for x in l:
    k += 1
    sm_nepovt = 0
    pr_povt = 1
    for n in x:
        if x.count(n) == 1:
            sm_nepovt += n
        else:
            pr_povt *= n
    if 3 * sm_nepovt >= pr_povt:
        if (x[0] % 2 == 0 and x[1] % 2 != 0 and x[2] % 2 == 0 and x[3] % 2 != 0 and x[4] % 2 == 0 and x[5] % 2 != 0 and x[6] % 2 == 0) or \
                (x[0] % 2 != 0 and x[1] % 2 == 0 and x[2] % 2 != 0 and x[3] % 2 == 0 and x[4] % 2 != 0 and x[5] % 2 == 0 and x[6] % 2 != 0):
            sm += k
print(sm)