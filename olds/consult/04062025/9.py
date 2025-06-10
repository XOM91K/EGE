l = [[int(d) for d in x.split()] for x in open('9.txt')]
sm = 0
for x in l:
    k = 0
    povt3 = [y for y in x if x.count(y) == 3]
    povt2 = [y for y in x if x.count(y) == 2]
    povt1 = [y for y in x if x.count(y) == 1]
    if x == sorted(x)[::-1]:
        k += 1
    if len(povt3) == 3 and len(povt2) == 2 and len(povt1) == 1:
        k += 1
    if len(povt3) > 0 and len(povt2) > 0 and min(povt3 + povt2) > povt1[0]:
        k += 1
    if k == 3:
        sm += sum(x)
print(sm)