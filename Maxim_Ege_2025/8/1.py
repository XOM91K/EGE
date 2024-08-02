import itertools
k = 0
for x in itertools.product('УОА', repeat=5):
    x = ''.join(x)
    k += 1
    print(x)
