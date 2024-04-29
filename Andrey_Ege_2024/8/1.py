import itertools
a = 0
for x in itertools.product('УОА', repeat=5):
    a += 1
    x = ''.join(x)
    if a == 240:
        print(x)