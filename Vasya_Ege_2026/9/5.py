l = [[int(d) for d in x.split()] for x in open('5.txt')]
for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    povt2 = [d for d in x if x.count(d) == 2]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt3) == 3 and len(povt2) == 2 and len(povt1) == 3:
        if sum(povt3) + sum(povt2) > sum(povt1):
            print(x, sum(x))