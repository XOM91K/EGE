import itertools
ct = 0
for x in itertools.product('КРЕМНИЙ', repeat=5):
    x = ''.join(x)
    if x.count('Й') <= 2:
        if (x.count('Е') + x.count('И')) != 0 and (x.count('Е') + x.count('И')) % 2 == 0:
            ct += 1
            print(x)
print(ct)
#print(0 % 2)