import itertools

ct = 0
su = 0
for x in itertools.product('аекптч', repeat=7):
    x = ''.join(x)
    ct += 1
    if 'аптечка' in x:
        print(ct)
    if 'печатка' in x:
        print(ct)
print(154381 - 28921 - 1)