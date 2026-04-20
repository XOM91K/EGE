l = [[int(d) for d in x.split()] for x in open('5.txt')]
l = sorted(l, key=lambda d: sum(d))
square_time = 0
poed = []
for x in l:
    if x[0] >= square_time:
        square_time = sum(x)
        poed.append(x)
print(len(poed))
for x in poed:
    print(x, sum(x))
for x in l:
    if x[0] > 1384:
        print(x)
print(1397 - 1375)