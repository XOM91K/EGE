l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    x.sort()
    # 16 16 17 17 18 19
    povt2 = [d for d in x if x.count(d) == 2]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt2) == 4 and len(povt1) == 2:
        if sum(povt2) // 2 < sum(povt1):
            ct += 1
print(ct)