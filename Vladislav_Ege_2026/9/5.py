l = [[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
for x in l:
    if x.count(min(x)) == 1:
        povt = [d for d in x if x.count(d) > 1]
        if len(povt) > 0:
            x.sort()
            if x[0] + x[-1] < sum(povt):
                ct += 1
print(ct)