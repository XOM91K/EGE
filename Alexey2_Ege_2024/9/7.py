l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    if len(set(x)) < 6:
        if x.count(max(x)) == 1:
            povt = []
            for y in x:
                if x.count(y) > 1:
                    povt.append(y)
            if sum(povt) < sum(x) - sum(povt):
                print(x, povt)
                ct += 1
print(ct)