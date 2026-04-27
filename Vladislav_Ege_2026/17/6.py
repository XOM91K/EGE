l = [int(x) for x in open('6.txt')]
mx = []
ln4 = len([d for d in l if len(str(abs(d))) == 4 and str(d)[-1] == '3'])
for x in range(len(l) - 2):
    tr = sorted([d for d in [l[x], l[x + 1], l[x + 2]]])
    if tr[-1] + tr[-2] > ln4 ** 2:
        mx.append(abs(l[x] + l[x + 1] + l[x + 2]))
print(len(mx), max(mx))
