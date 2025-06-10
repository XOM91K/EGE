import itertools
ct = 0
for i in itertools.product('0123456789AB', repeat=5):
    i = ''.join(i)
    if i.count('3') == 1 and i[0] != '0':
        i = i.replace('0', '*')
        i = i.replace('1', '#')
        i = i.replace('2', '*')
        i = i.replace('3', '#')
        i = i.replace('4', '*')
        i = i.replace('5', '#')
        i = i.replace('6', '*')
        i = i.replace('7', '#')
        i = i.replace('8', '*')
        i = i.replace('9', '#')
        i = i.replace('A', '*')
        i = i.replace('B', '#')
        if i == '#*#*#' or i == '*#*#*':
            ct += 1
print(ct)
