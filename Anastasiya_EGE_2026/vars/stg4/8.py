import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        for y in '02468a':
            if y + y + y in x:
                break
        else:
            continue
        ch = [d for d in x if d in '02468a']
        if len(ch) == 3:
            ct += 1
print(ct)