import itertools
ct = 0
for x in itertools.product('ГЕКЭ023', repeat=4):
    x = ''.join(x)
    ct += 1
    if x[0] in '203':
       if "КК" not in x and "ЕЕ" not in x and "ГГ" not in x and "ЭЭ" not in x and "22" not in x and "00" not in x and "33" not in x:
         print(ct, x)