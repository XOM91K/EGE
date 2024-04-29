import itertools

ct = 0
su = 0
for x in itertools.product(sorted('привычка'), repeat=5):
    x = ''.join(x)
    ct += 1
    if ct % 5 != 0:
        su += 1
        if len(set(x)) == 5:
            if 'а' not in x and 'и' not in x and 'ы' not in x:
                print(su)
                break