l = [int(x) for x in open('2.txt')]
mn7 = min([x for x in l if str(x)[-1] == '7'])
pr = []
for x in range(len(l) - 2):
    if len(str(abs(l[x]))) == 5 or len(str(abs(l[x + 1]))) == 5 or len(str(abs(l[x + 2]))) == 5:
        if (l[x] * l[x + 1] * l[x + 2]) % mn7 == 0:
            pr.append(l[x] * l[x + 1] * l[x + 2])
print(len(pr), max(pr))