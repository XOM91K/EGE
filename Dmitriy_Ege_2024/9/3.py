l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    sm_nch = sum([y for y in x if y % 2 != 0])
    sm_ch = sum([y for y in x if y % 2 == 0])
    if (len(set(x)) == 4 and sm_nch <= sm_ch) or (len(set(x)) != 4 and sm_nch > sm_ch):
        ct += 1
print(ct)