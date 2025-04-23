l = [int(x) for x in open('2.txt')]
mx4 = max([x for x in l if len(str(abs(x))) == 4])
mx = []
for x in range(len(l) - 1):
    if abs(l[x] - l[x + 1]) >= mx4:
       mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))