import itertools
ct = 0
for x in itertools.product('012345', repeat=3):
    x = ''.join(x)
    if x[0] != '0':
        if x.count('5') == 1:
            if x.count('25') == 0 and x.count('52') == 0 and x.count('45') == 0 and x.count('54') == 0 and x.count('05') == 0 and x.count('50') == 0:
                ct += 1
print(ct)