import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('4') == 2 and '14' not in x and '41' not in x and '34' not in x and '43' not in x and '54' not in x and '45' not in x and '74' not in x and '47' not in x and '94' not in x and '49' not in x and 'b4' not in x and '4b' not in x:
        ct += 1
print(ct)