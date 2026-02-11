l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt1) == 5:
        ch = [d for d in x if d % 2 == 0]
        nch = [d for d in x if d % 2 != 0]
        if len(nch) > len(ch):
            if sum(nch) < sum(ch):
                ct += 1
print(ct)