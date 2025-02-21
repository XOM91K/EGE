l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    k = 0
    if len(set(x)) == 4:
        k += 1
    ch = [i for i in x if i % 2 == 0]
    nch = [i for i in x if i % 2 != 0]
    if sum(nch) > sum(ch):
        k += 1
    if k == 1:
        ct += 1
print(ct)