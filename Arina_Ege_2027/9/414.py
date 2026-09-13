l = [[int(d) for d in x.split()] for x in open('414.txt')]
ct = 0
for x in l: # 4 4 4 6 7 9
    povt3 = [d for d in x if x.count(d) == 3]
    povt1 = [d for d in x if x.count(d) == 1]
    povt = [d for d in x if x.count(d) > 1]
    if len(povt3) == 3 and len(povt1) == 3:
        if sum(povt1) / len(povt1) < sum(povt):
            ct += 1
print(ct)