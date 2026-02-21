import itertools, string
ct2 = 0
for x in itertools.product('0123456789' + string.ascii_uppercase[:15], repeat=4):
    x = ''.join(x)
    if x[0] != '0':
        can = False
        for y in ('0123456789' + string.ascii_uppercase[:15])[::2]:
            if y in x:
                can = True
                break
        if can:
            ct = 0
            for y in string.ascii_uppercase[6:]:
                ct += x.count(y)
            if ct > 2 :
                ct2 += 1
print(ct2)