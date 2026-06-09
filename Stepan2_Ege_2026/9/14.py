l = [[int(d) for d in x.split()] for x in open('14.txt')]
ct = 0
for x in l:
    x = sorted(x)
    if x.count(x[6]) == 1:
        povt2 = [d for d in x if x.count(d) > 1]
        if len(povt2) > 0:
            povt1 = [d for d in x if x.count(d) == 1]
            if len(povt2) > 0:
                if sum(povt2) * 3 <= sum(povt1) :
                    ct += 1
print(ct)