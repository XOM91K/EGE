l = [[int(d) for d in x.split()] for x in open('17.txt')]
ct = 0
for x in l:
    x = sorted(x)
    if x.count(x[-1]) == 1:
        povt = [d for d in x if x.count(d) > 1]
        if len(povt) > 0:
            if x[-1] > 3*((sum(x) - x[-1])/(len(x)-1)):
                ct += 1
print(ct)