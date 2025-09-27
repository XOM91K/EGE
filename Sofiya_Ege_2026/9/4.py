l=[[int(d) for d in x.split()] for x in open('4.txt')]
ct=0
for x in l:
    nch = [a for a in x if a % 2 != 0]
    ch = [a for a in x if a % 2 == 0]
    k = 0
    if len(set(x))==4:
        k += 1
    if sum(nch) > sum(ch):
        k += 1
    if k == 1:
        ct += 1
print(ct)