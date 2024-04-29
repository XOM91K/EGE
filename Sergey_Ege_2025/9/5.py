l = [[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
for x in l:
    povt = sum(x) - sum(set(x))
    sr_ar = (sum(x) - povt * 2) / 4
    if len(set(x)) == 5 and sr_ar <= povt * 2:
        ct += 1
print(ct)