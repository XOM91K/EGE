l = [int(x) for x in open('17.txt')]
kvmax2 = max([d for d in l if len(str(d)) == 2 and str(d)[-1] == '3'])
mx = []
for x in range(len(l) - 2):
    if l[x] < 0 and l[x + 1] < 0 and l[x + 2] < 0:

        if len(str(abs(l[x]))) != 3 and len(str(abs(l[x]))) != 3 and len(str(abs(l[x]))) != 3:

            if abs(min(l[x], l[x + 1], l[x + 2])) + abs(max(l[x], l[x + 1], l[x + 2])) <= kvmax2 ** 2:
                mx.append(abs(min(l[x], l[x + 1], l[x + 2])) + abs(max(l[x], l[x + 1], l[x + 2])))
print(len(mx), max(mx))
