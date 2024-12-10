l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        otr = []
        pol = []
        for y in x:
            if y < 0:
                otr.append(y)
            else:
                pol.append(y)
        if abs(sum(otr)) > sum(pol):
            ct += 1
print(ct)