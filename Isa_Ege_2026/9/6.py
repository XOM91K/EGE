l=[[int(d) for d in x.split()] for x in open('6.txt')]
ct=0
for x in l:
    povt2 = [m for m in x if x.count(m) == 2]
    povt1 = [b for b in x if x.count(b) == 1]
    kr2 = [s for s in x if s % 2 == 0]
    k = 0
    if (len(set(x))==4 and len(povt2)==2):
        k += 1
    if sum(kr2)< sum(x)-sum(kr2):
        k += 1
    if k == 1:
        ct += 1

print(ct)
# 511 - 29 = 482