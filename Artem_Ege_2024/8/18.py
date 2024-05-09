import itertools
ct =0
for x in itertools.product('012345678', repeat=7):
    x = ''.join(x)
    if x[0] not in '01357' and x[-1] in '0124578' and '6' in x:
        ct += 1
print(ct)