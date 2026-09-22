import itertools
def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    if s == '':
        return '0'
    return s[::-1]
ct = 0
for z in range(1, 13):
    for x in itertools.product('012', repeat=z):
        x = ''.join(x)
        tr = sum(map(int, v3(int(x))))
        if x[0] != '0' and int(x) % tr == 0:
            x = x.replace('2', '0')
            if x.count('01') + x.count('10') > 3:
            #k = 0
            # for y in range(len(x) - 1):
            #     if x[y] != x[y + 1]:
            #         k += 1
            # if k > 3:
                ct += 1
print(ct)
    # 23232 # 0101011