import itertools
ct = 0
for x in itertools.product('01234567', repeat=6):
    x = ''.join(x)
    if x[0] != '0' and x == x[::-1]:
        if sum([int(d) for d in x if int(d) % 2 == 0]) <= sum([int(d) for d in x if int(d) % 2 != 0]):
            ct += 1
print(ct)