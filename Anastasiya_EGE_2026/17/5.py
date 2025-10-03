l = [int(x) for x in open('5.txt')]
mx8 = max([y for y in l if str(abs(y))[0] == '8'])
mn = []
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
            mn.append(l[x] + l[x + 1] + l[x + 2])
print(len(mn), min(mn))