l = [[int(d) for d in x.split()] for x in open('5.txt')]
k = 0
sm = 0
for x in l:
    k += 1
    if len(set(x)) < len(x):
        povt = []
        for y in x:
            if x.count(y) != 1:
                povt.append(y)
        if (sum(povt) * len(x)) < (sum(x) * len(povt)):
            sm += k
print(sm)
