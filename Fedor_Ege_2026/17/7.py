l = [int(x) for x in open('7.txt')]
mi = min([y for y in l if y > 0 and str(y)[-1] == '4'])
xy = []
for x in range (len(l)-2):
    smcif1 = sum([int(b) for b in str(abs(l[x]))])
    smcif2 = sum([int(b) for b in str(abs(l[x + 1]))])
    smcif3 = sum([int(b) for b in str(abs(l[x + 2]))])
    if smcif1 + smcif2 + smcif3 == mi:

        xy.append(l[x] + l[x + 1] + l[x + 2])
print(len(xy), max(xy))