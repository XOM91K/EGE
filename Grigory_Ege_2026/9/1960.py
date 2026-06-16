l = [[int(d) for d in x.split()] for x in open('1960.txt')]
ct = 0
for x in l:
    povt = [y for y in x if x.count(y) > 1]
    nepovt = [y for y in x if x.count(y) == 1]
    k = 0
    if len(povt) > 1 and len(nepovt) >= 1:
        k += 1
    if len(povt) > 0 and (sum(povt)/len(povt)) > min(x):
        k += 1
    x = sorted(x)
    if x[0] + x[-1] != x[1] + x[2]:
        k += 1
    if k >= 2:
        ct += 1
print(ct)