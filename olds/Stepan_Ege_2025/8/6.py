import itertools
l = 0
ct = 0
for x in itertools.product('АБОРСУЭ', repeat=5):
    x = ''.join(x)
    l += 1
    if l % 2 == 0 and x.count('Р') >= 2 and ('РАР' in x or 'РСР' in x or 'РОР' in x or 'РЭР' in x or 'РБР' in x) and x.count('У') == 0:
        ct += 1
print(ct)

