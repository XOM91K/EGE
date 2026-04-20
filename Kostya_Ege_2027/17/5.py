l = [int(x) for x in open('5.txt')]
ln3 = len([d for d in l if str(abs(d))[-1] == '3' and len(str(abs(d))) == 4])
mx = []
for x in range(len(l) - 2):
    tr = sorted([l[x], l[x + 1], l[x + 2]])
    if tr[-1] + tr[-2] > ln3 ** 2:
        mx.append(sum(tr))
print(len(mx), max(mx))
