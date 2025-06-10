l = [int(x) for x in open('15.txt')]
mx7 = max([x for x in l if str(x)[-1] == '7'])
sm = []
for x in range(len(l) - 1):
    if l[x] + l[x + 1] < mx7:
        if str(l[x])[0] == str(l[x + 1])[0]:
            if (str(l[x])[-1] == '7' and len(str(abs(l[x]))) == 3) or (str(l[x + 1])[-1] == '7' and len(str(abs(l[x + 1]))) == 3):
                sm.append(l[x] + l[x + 1])
print(len(sm), max(sm))