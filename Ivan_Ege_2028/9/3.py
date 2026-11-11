l = [[int(d) for d in x.split()] for x in open('3.txt')]
for x in l:
    povt1 = [d for d in x if x.count(d) == 1]
    povt2 = [d for d in x if x.count(d) == 2]
    povt3 = [d for d in x if x.count(d) == 3]
    if len(povt3) == 3 and len(povt2) == 2 and len(povt1) == 3:
        if sum(povt2) + sum(povt3) > sum(povt1):
            print(sum(x))