l = [[int(d) for d in x.split()] for x in open('9.txt')]
for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    povt2 = [d for d in x if x.count(d) == 2]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt3) == 3 and len(povt2) == 2 and len(povt1) == 2:
        if sum(povt1) <= min(povt3 + povt2):
            print(x)
# print([33, 33, 33] + [44, 44])