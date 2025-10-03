l = [int(x) for x in open('3.txt')]
mx7 = max([x for x in l if str(x)[-1] == '7'])
mx = []
for x in range(len(l) - 1):
    if str(l[x])[0] == str(l[x + 1])[0]:
        if (len(str(l[x])) == 3 and str(l[x])[-1] == '7') or (len(str(l[x + 1])) == 3 and str(l[x + 1])[-1] == '7'):
            if l[x] + l[x + 1] < mx7:
                mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))