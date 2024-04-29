ct = 0
k = 0
l = [[int(d) for d in x.split()]for x in open('7.txt')]
for x in l:
    k += 1
    povt = []
    if len(set(x)) != len(x):
        for y in x:
            if x.count(y) > 1:
                povt.append(y)
            if len(povt) != 0 and (sum(povt) / len(povt)) < (sum(x) / len(x)):
                ct += k
print(ct)