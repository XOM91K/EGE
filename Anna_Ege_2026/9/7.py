l =[[int(d) for d in x.split()] for x in open('7.txt')]
k = 0
for x in l:
    k += 1
    povt2 = [y for y in x if x.count(y) == 2]
    povt1 = [y for y in x if x.count(y) == 1]
    if len(povt2) == 4 and len(povt1) == 3:
        if sum(povt2) / len(povt2) < max(povt1):
            print(k)
            break