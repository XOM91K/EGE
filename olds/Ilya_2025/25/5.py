import fnmatch, itertools
ct = 0
sm = 0
for y in range(7):
    for x in itertools.product('0123456789', repeat=y):
        x = ''.join(x)
        for z in range(10):
            d = int('1' + x + '28' + str(z) + '64')
            if d <= 10 ** 12 and d % 596 == 0:
                ct += 1
                sm += d
print(ct, sm // ct)

# for x in range(596, 10 ** 12, 596):
#     if fnmatch.fnmatch(str(x), '1*28?64'):
#         ct += 1
#         sm += x
# print(ct, sm // ct)