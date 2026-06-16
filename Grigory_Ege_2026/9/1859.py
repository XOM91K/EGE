l = [[int(d) for d in x.split()] for x in open('1859.txt')]
for x in l:
    povt3 = [y for y in x if x.count(y) == 3]
    povt1 = [y for y in x if x.count(y) == 1]
    if len(povt3) == 6 and len(povt1) == 1:
        if povt1[0] <= min(povt3):
            print(x)