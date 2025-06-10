import itertools
ct = 0
for x in set(itertools.product('СВЯТОСЛАВ', repeat=7)):
    x = ''.join(x)
    gl = 0
    sg = 0
    for y in x:
        if y in 'ЯОА':
            gl += 1
        else:
            sg += 1
    if gl > sg:
        ct += 1
print(ct)