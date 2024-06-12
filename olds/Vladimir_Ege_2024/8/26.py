import itertools
k = 0
ct = 0
for x in itertools.product(sorted('АЭРОБУС'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x.count('Р') >= 2:
        if 'РРР' not in x and ('РАР' in x or 'РСР' in x or 'РЭР' in x or 'РОР' in x or 'РБР' in x or 'РУР' in x):
            if 'У' not in x:
                ct += 1
print(ct)