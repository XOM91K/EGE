l = sorted([[int(d) for d in x.split()] for x in open('12.txt')])
mx_ct = 0
ct_ct = 0
mas = []
for x in range(0, 1442):
    ct = 0
    for y in l:
        if y[0] <= x < y[1]:
            ct += 1
    mx_ct = max(mx_ct, ct)
for x in range(0, 1442):
    ct = 0
    for y in l:
        if y[0] <= x < y[1]:
            ct += 1
    if ct == mx_ct:
        print(x)
print(mx_ct)