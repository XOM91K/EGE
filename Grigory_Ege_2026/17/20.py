l = [int(x) for x in open('20.txt')]
mx28 = max([y for y in l if str(y)[-2:] == '28'])
mx = []
for x in range(len(l) - 2):
    if len(str(abs(l[x]))) == 3 or len(str(abs(l[x + 1]))) == 3 or len(str(abs(l[x + 2]))) == 3:
        if (l[x] + l[x + 1] + l[x + 2]) / 3 > 0 and (l[x] + l[x + 1] + l[x + 2]) / 3 < mx28:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))