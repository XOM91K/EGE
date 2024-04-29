import itertools
ct = 0
s = 'ВОЛК'
for x in itertools.product('ПОЛЯКВ', repeat=4):
    x = ''.join(x)
    k = 0
    for y in range(len(s)):
        if x[y] == s[y]:
            k += 1
    if k == 2:
        print(x)
        ct += 1
print(ct)