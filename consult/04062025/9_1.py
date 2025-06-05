l = [[int(d) for d in x.split()] for x in open('9_1.txt')]
k = 0
for x in l:
    k += 1
    if k % 7 == 0:
        if x == sorted(x):
            povt4 = [y for y in x if x.count(y) == 4]
            povt2 = [y for y in x if x.count(y) == 2]
            povt1 = [y for y in x if x.count(y) == 1]
            if len(povt4) == 4 and len(povt2) == 2 and len(povt1) == 1:
                if max(povt4 + povt2) <= povt1[0]:
                    print(k)
                    break