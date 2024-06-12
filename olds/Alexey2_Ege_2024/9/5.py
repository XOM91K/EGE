l = [[int(d) for d in x.split()] for x in open('5.txt')]
k = 0
sm = 0
for x in l:
    k += 1
    povt = []
    for y in x:
        if x.count(y) > 1:
            povt.append(y)
    if len(povt) > 0 and sum(povt) / len(povt) < sum(x) / len(x):
        sm += k
print(sm)