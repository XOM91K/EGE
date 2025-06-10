l = [int(x) for x in open('17.txt')]
mx4 = max([x for x in l if len(str(abs(x))) == 4 and str(x)[-1] == '5' and x > 0])
mx = []
for x in range(len(l) - 1):
    if (len(str(abs(l[x]))) == 4 and str(l[x])[-1] == '5') or (len(str(abs(l[x + 1]))) == 4 and str(l[x + 1])[-1] == '5'):
        if l[x] + l[x + 1] > mx4:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))
