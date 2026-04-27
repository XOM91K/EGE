l = [[int(d) for d in x.split()] for x in open('20.txt')]
ct = 0
for x in l:
    if x[0] < x[1] < x[2] < x[3] < x[4]:
        if (x[0] + x[-1]) <= (x[1] + x[2] + x[3]):
            ct += 1
print(ct)