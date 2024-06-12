import itertools
ct = 0
su = 0
for x in itertools.product('еикрсуя', repeat=6):
    x = ''.join(x)
    ct += 1
    if x[0] not in "к" and (x.count('е') + x.count('у') + x.count("и") + x.count('я')) <= 2:
        if ct % 2 == 0:
            su += 1
print(su)