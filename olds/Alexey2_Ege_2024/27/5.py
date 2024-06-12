l = [sorted([int(d) for d in x.split()]) for x in open('5.txt')]
mx_sm = 0
mn_rzn = 10 ** 10
d = 91
for x in l:
    mx_sm += x[-1]
    if (x[-1] - x[0]) % d != 0:
        mn_rzn = min(mn_rzn, (x[-1] - x[0]))
    if (x[-1] - x[1]) % d != 0:
        mn_rzn = min(mn_rzn, (x[-1] - x[1]))
if mx_sm % d == 0:
    print(mx_sm - mn_rzn)
else:
    print(mx_sm)