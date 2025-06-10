l = [[int(d) for d in x.split()] for x in open('10.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        otr = 0
        pol = 0
        for y in x:
            if y > 0:
                pol += y
            else:
                otr += y
        if abs(otr) > pol:
            ct += 1
print(ct)