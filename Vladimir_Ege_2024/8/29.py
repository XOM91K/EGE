import itertools
ct = 0
for x in itertools.product('012345678', repeat=6):
    x = ''.join(x)
    if x[0] != '0' and x.count('4') == 1:
        if '14' not in x and '41' not in x and '34' not in x and '43' not in x and '54' not in x and '45' not in x and '74' not in x and '47' not in x:
            ct += 1
print(ct)