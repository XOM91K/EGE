l = [int(x) for x in open('11.txt')]
mx43 = max([d for d in l if str(d)[-2:] == '43' and len(str(abs(d))) == 4]) ** 2
print(mx43 ** 0.5)
mx = []
for x in range(len(l) - 1):
    if len(str(abs(l[x]))) == 4 or len(str(abs(l[x + 1]))) == 4:
        if (l[x] + l[x + 1]) ** 2 < mx43:
            mx.append((l[x] + l[x + 1]) ** 2)
print(len(mx), max(mx))