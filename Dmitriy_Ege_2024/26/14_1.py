l = sorted([[int(d) for d in x.split()] for x in open('14.txt')])
start = 0
finish = []
ct_p = 0
for x in l:
    ct = 1
    for y in finish:
        if x[0] <= y:
            ct += 1
    finish.append(x[1])
    ct_p = max(ct_p, ct)
start = 0
finish = []
ct_u = 0
for x in l:
    ct = 1
    for y in finish:
        if x[0] <= y:
            ct += 1
    finish.append(x[1])
    if ct == ct_p:
        ct_u += 1
print(ct_u, ct_p)