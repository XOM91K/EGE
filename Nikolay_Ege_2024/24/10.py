s = open('10.txt').readlines()
d = 1
for x in s:
    while 'XYZ' * d in x:
        d += 1
print((d - 1) * 3)