import itertools
ct = 0
for x in itertools.product('012345678', repeat=4):
    x = ''.join(x)
    if x[0] != '0' and x.count('6') <= 2: #and '06' not in x and '60' not in x and '26' not in x and '62' not in x and '46' not in x and '64' not in x and '86' not in x and '68' not in x and '66' not in x:
        # x = x.replace('0', '$')
        # x = x.replace('2', '$')
        # x = x.replace('4', '$')
        # x = x.replace('8', '$')
        for y in '0248':
            x = x.replace(y, '$')
        if '$6' not in x and '6$' not in x and '66' not in x:
            ct += 1
            print(x)
print(ct)