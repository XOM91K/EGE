l = [[int(d) for d in x.split()] for x in open('4.txt')]
ct = 0
for x in l:
    k = 0
    povt2 = [d for d in x if x.count(d) == 2]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt2) == 2 and len(povt1) ==  3:
        k += 1
    ch = [d for d in x if d % 2 == 0]
    nch = [d for d in x if d % 2 != 0]
    if sum(nch) > sum(ch):
        k += 1
    if k == 1:
        ct += 1
print(ct)