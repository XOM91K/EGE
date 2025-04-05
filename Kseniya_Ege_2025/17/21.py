l = [int(x) for x in open('21.txt')]
mn7 = min([x for x in l if str(x)[-1] == '7'])
mx = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5:
        k += 1
    if len(str(abs(l[x + 1]))) == 5:
        k += 1
    if len(str(abs(l[x + 2]))) == 5:
        k += 1
    if k >= 1:
        if (l[x] * l[x + 1] * l[x + 2]) % mn7 == 0:
            mx.append(l[x] * l[x + 1] * l[x + 2])
print(len(mx), max(mx))
