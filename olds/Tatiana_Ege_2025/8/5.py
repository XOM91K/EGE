import itertools
a = itertools.product('012345', repeat=3)
w = 0
for i in a:
    h = "".join(i)
    if h.count('5') == 1 and h[0] != '0':
        if '05' not in h and '50' not in h and '25' not in h and '52' not in h and '45' not in h and '54' not in h:
            w += 1
print(w)