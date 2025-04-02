l = [int(x) for x in open('13.txt')]
mn7 = min([x for x in l if str(x)[-1] == '7'])
mx = []
for x in range(len(l) - 2):
    if len(str(abs(l[x]))) == 5 or len(str(abs(l[x + 1]))) == 5 or len(str(abs(l[x + 2]))) == 5:
        if l[x] * l[x + 1] * l[x + 2] % mn7 == 0:
            mx.append(l[x] * l[x + 1] * l[x + 2])
print(len(mx), max(mx))