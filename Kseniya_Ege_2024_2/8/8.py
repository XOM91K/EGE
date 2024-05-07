import itertools
ct = 0
for x in itertools.product('ВОЗДУХ', repeat = 5):
    x = ''.join(x)
    if x.count('О') + x.count('У') ==1:
        if 'ВО' not in x and 'ВУ' not in x and 'ХО' not in x and 'ХУ' not in x:
            if 'ОВ' not in x and 'УВ' not in x and 'ОХ' not in x and 'УХ' not in x:
                ct += 1
print(ct)