import itertools
ct = 0
for x in itertools.product('01234567', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('3') <= 1:
        x = x.replace('1', '9')
        x = x.replace('3', '9')
        x = x.replace('5', '9')
        x = x.replace('7', '9')
        if '99' not in x:
            ct +=1
            print(x)
print(ct)