import itertools
cnt = 0
for x in itertools.product('01234567', repeat = 5):
    w = ''.join(x)
    if w[0] not in '01357' and x[-1] not in '26':
            if w.count('7') <= 2:
                cnt += 1
print(cnt)