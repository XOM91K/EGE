l = [int(x) for x in open('5.txt')]
ct = 0
mn = []
mx8 = max([d for d in l if str(abs(d))[0] == '8'])
for x in range(len(l) - 2):
    k = 0
    if str(abs(l[x]))[0] == '6':
        k += 1
    if str(abs(l[x + 1]))[0] == '6':
        k += 1
    if str(abs(l[x + 2]))[0] == '6':
        k += 1
    if k <= 1:
        if l[x] + l[x + 1] + l[x + 2] >= mx8:
            ct += 1
            mn.append(l[x] + l[x + 1] + l[x + 2])
print(ct, min(mn))