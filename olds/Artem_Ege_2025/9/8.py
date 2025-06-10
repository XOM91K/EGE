l = [[int(d) for d in x.split()] for x in open('8.txt')]
ct = 0
for x in l:
    ch = [d for d in x if d % 2 == 0]
    nch = [d for d in x if d % 2 != 0]
    k = 0
    if len(set(x)) == 4:
        k += 1
    if sum(nch) > sum(ch):
        k += 1
    if k == 1:
        ct += 1
print(ct)