import itertools

ct = 0
for x in itertools.product('012345678', repeat=7):
    x = ''.join(x)
    if x[0] != '0' and x[-1] not in '347' and '000' not in x and '111' not in x and '222' not in x and '333' not in x and '444' not in x and '555' not in x and '666' not in x and '777' not in x and '888' not in x:
        ct += 1
print(ct)
