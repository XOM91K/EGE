l = [[int(d) for d in x.split()] for x in open('4.txt')]
ct = 0
for x in l:
    povt3 = [c for c in x if x.count(c) == 3]
    povt1 = [c for c in x if x.count(c) == 1]
    if len(povt3) == 3 and len(povt1) == 3:
        if sum(povt1) / 3 < sum(povt3):
    # if len(povt3) == 3 and len(set(x)) == 4:
    #     if (sum(x) - sum(povt3)) / 3 < sum(povt3):
            ct += 1
print(ct)