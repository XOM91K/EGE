import itertools
ct=0
for x in itertools.product('01234567', repeat=5):
    x = ''.join(x)
    if x.count('3') <= 1:
        x = x.replace('1', '#')
        x = x.replace('3', '#')
        x = x.replace('5', '#')
        x = x.replace('7', '#')
        if x[0] != '0' and '##' not in x:
            ct+=1
print(ct)