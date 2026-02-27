import itertools
ct = 0
for x in itertools.product('012345678', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('0') == 1:
        for y in '1357':
            x = x.replace(y, '#')
        if '#0' not in x and '0#' not in x:
            ct += 1
print(ct)