import itertools
k = '02468ace'
n = '0369c'
ct = 0
for x in itertools.product('0123456789abcde', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        if x[0] in k and x[1] in n and x[2] in k and x[3] in n and x[4] in k:
            ct += 1
        elif x[0] in n and x[1] in k and x[2] in n and x[3] in k and x[4] in n:
            ct += 1
print(ct)