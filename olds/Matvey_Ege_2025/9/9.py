l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        otr = []
        pol = []
        for i in x:
            if i < 0:
                otr.append(abs(i))
            else:
                pol.append(i)
        if sum(otr) > sum(pol):
            ct += 1
print(ct)