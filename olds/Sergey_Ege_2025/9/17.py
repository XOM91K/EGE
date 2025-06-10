l = [[int(d) for d in x.split()] for x in open('17.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        otr = []
        pol = []
        for y in range(6):
            if x[y] > 0:
                pol.append(x[y])
            else:
                otr.append(x[y])
        if abs(sum(otr)) > sum(pol):
            ct += 1
print(ct)