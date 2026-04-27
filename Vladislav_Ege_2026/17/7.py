l = [int(x) for x in open('7.txt')]
mx = max([d for d in l if len(str(abs(d))) == 5 and str(d)[-1] == '3'])
k = []
for x in range(len(l) - 2):
    h = [d for d in [l[x], l[x + 1], l[x + 2]] if len(str(abs(d))) == 5 and str(d)[-1] == '3']
    if len(h) >= 2:
        if l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2 <= mx ** 2:
            k.append(l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2)
print(len(k), min(k))