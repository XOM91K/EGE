#ДЕРЕВО
# gr1 = s[::2]
# gr2 = s[1::2]
# if ord(gr1[0]) <= ord(gr1[1]) <= ord(gr1[2]):
#     if ord(gr2[0]) <= ord(gr2[1]) <= ord(gr2[2]):
ct =  0
import itertools
for x in set(itertools.product('ДЕРЕВО', repeat=6)):
    x = ''.join(x)
    gr1 = x[::2]
    gr2 = x[1::2]
    if ord(gr1[0]) <= ord(gr1[1]) <= ord(gr1[2]):
        if ord(gr2[0]) <= ord(gr2[1]) <= ord(gr2[2]):
            ct += 1
print(ct)