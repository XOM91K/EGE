l =[[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
for x in l:
    ch = [y for y in x if y % 2 == 0]
    nch = [y for y in x if y % 2 != 0]
    k = 0
    if len(set(x)) == 4:
        k += 1
    if ( sum(nch) > sum(ch)):
        k += 1
    if k == 1:
         ct += 1
print(ct)
# 29 511