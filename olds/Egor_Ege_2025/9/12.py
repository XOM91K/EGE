l = [[int(d) for d in x.split()] for x in open('12.txt')]
sm = 0
for x in l:
    if x == sorted(x)[::-1]:
        povt3 = [y for y in x if x.count(y) == 3]
        povt2 = [y for y in x if x.count(y) == 2]
        povt1 = [y for y in x if x.count(y) == 1]
        if len(povt3) == 3 and len(povt2) == 2 and len(povt1) == 1:
            if min(povt3 + povt2) > povt1[0]:
                sm += sum(x)
print(sm)