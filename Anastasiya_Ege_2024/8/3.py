from itertools import *
ct = 0
for x in product('014689acefg', repeat=6):
    x = ''.join(x)
    if len(set(x)) == len(x):
        if x[0] in '468aceg':
            ct += 1
print(ct)