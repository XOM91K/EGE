l = [sorted([int(d) for d in x.split()]) for x in open('15.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        pol = []
        otr = []
        for y in x:
            if y > 0:
                pol.append(y)
            else:
                otr.append(y)
        if abs(sum(otr)) > sum(pol):
            ct += 1
print(ct)