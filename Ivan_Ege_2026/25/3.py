import itertools
for x in range(0, 5):
    for y in itertools.product('0123456789', repeat=x):
        y = ''.join(y)
        for z in range(0, 10):
            a = '32' + y + '54' + str(z) + '123'
            if int(a) % 519 == 0 and int(a) < 10 ** 13:
                if len(a) % 2 == 0 and '0' not in a:
                    a1 = a[:len(a)//2]
                    a2 = a[len(a)//2:]
                    if sum(map(int, a1)) == sum(map(int, a2)):
                        print(int(a), int(a)//519)
# import fnmatch
# for i in range(51900000, 10**13, 519):
#     a = str(i)
#     if fnmatch.fnmatch(a, '32*54?123'):
#         if len(a) % 2 == 0 and '0' not in a:
#             a1 = a[:len(a)//2]
#             a2 = a[len(a)//2:]
#             if sum(map(int, a1)) == sum(map(int, a2)):
#                 print(i, i//519)