import itertools
ct = 0
for x in itertools.product('012345', repeat=3):
    x = ''.join(x)
    if x.count('5') == 1 and x[0] != "0" and ((x[0] != '5' or x[1] not in '024') and (x[1] != '5' or ((x[0] not in '024' and x[2] not in "024"))) and (x[2] != '5' or x[1] not in '024')):
        ct += 1
        print(x)
print(ct)