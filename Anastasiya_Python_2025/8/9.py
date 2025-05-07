import itertools
ct = 0

for x in itertools.permutations(sorted('АПЕЛЬСИН'), 7):
    x = ''.join(x)
    x = x.replace('П', '#')
    x = x.replace('Л', '#')
    x = x.replace('С', '#')
    x = x.replace('Н', '#')
    if '#Ь#' in x or 'Ь' not in x:
        ct += 1
print(ct)
