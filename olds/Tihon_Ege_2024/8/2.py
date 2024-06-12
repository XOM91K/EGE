import itertools
ct = 0
for x in itertools.product('012345678', repeat=4):
    x = ''.join(x)
    if x.count('6') <= 2 and x[0] != '0':
        flag = True
        for y in '02468':
            if y+'6' in x or '6'+y in x:
                flag = False
        if flag == True:
            ct += 1
print(ct)