import itertools
ct = 0
for x in itertools.product('01234567', repeat=6):
    x = ''.join(x)
    ch = 0
    nch = 0
    for j in x:
        if int(j) % 2 == 0:
            ch += int(j)
        else:
            nch += int(j)
    if x[0] != '0' and x == x[::-1]  and ch <= nch:
        ct += 1
print(ct)