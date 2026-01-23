import itertools
ct = 0
for x in itertools.product('0123456789abcde', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('8') == 1 and (x.count('a') + x.count('b') + x.count('c') + x.count('d') + x.count('e')) >= 2:
      ct += 1
print(ct)