import itertools
ct = 0
for x in itertools.product('012345678', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('5') == 1:
        if x[0] != x[1] and x[1] != x[2] and x[2] != x[3] and x[3] != x[4]:
            ct += 1
print(ct)