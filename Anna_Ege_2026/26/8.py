l = [[int(d) for d in x.split()] for x in open('8.txt')]
l = sorted(l, key=sum)
print(l)
poed = []
arena = 0
for x in l:
    if x[0] >= arena:
        poed.append(x)
        arena = sum(x)
for x in l:
    if x[0] > 1364 and x[0] > 1391:
        print(x[0])
