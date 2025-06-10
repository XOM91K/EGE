l = [int(x) for x in open('8.txt')]
mx8 = max([x for x in l if str(abs(x))[0] == '8'])
mx = []
for x in range(len(l) - 2):
    n6 = [y for y in [l[x], l[x + 1], l[x + 2]] if str(abs(y))[0] == '6']
    if len(n6) <= 1:
        if l[x] + l[x + 1] + l[x + 2] >= mx8:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), min(mx))