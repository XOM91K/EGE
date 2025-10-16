import itertools
ct = 0
for x in itertools.product('0123456789ABCDE', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('8') == 1 and x.count('A') + x.count('B') + x.count('C') + x.count('D') + x.count('E') >= 2:
        ct +=1
print(ct)