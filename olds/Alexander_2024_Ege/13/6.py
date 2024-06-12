import itertools
ct = 0
for x in itertools.product('01', repeat=22):
    x = ''.join(x)
    if '111' in x:
        ct +=1
print(ct)