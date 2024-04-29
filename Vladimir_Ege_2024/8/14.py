import itertools
ct = 0
for x in itertools.product('012345678', repeat=4):
    x = ''.join(x)
    if x[0] != '0':
        if x.count('1') == 2:
            if '01' not in x and '10' not in x and '21' not in x and '12' not in x and '41' not in x and '14' not in x and '61' not in x and '16' not in x and '81' not in x and '18' not in x:
                print(x)
                ct += 1
print(ct)