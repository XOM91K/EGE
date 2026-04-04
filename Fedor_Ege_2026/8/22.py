import itertools
ct = 0
for x in itertools.product('012345678', repeat=4):
    x = ''.join(x)
    if x[0] != '0' and x.count('8') == 1:
        ind = x.index('8')
        lt = x[:ind]
        rt = x[ind + 1:]
        if sum(map(int, lt)) == sum(map(int, rt)):
            ct += 1
print(ct)
# print(sum(map(int, '')))