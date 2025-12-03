import fnmatch, itertools
for y in range(0, 6):
    for x in itertools.product('0123456789', repeat=y):
        x = ''.join(x)
        for z in range(10):
            s = '32' + x + '54' + str(z) + '123'
            if int(s) <= 10**13 and int(s) % 519 == 0 and '0' not in s and len(s) % 2 == 0:
                if sum(map(int, s[:len(s) // 2])) == sum(map(int, s[len(s) // 2:])):
                    print(int(s), int(s)//519)
# for x in range(519, 10**13, 519):
#     if fnmatch.fnmatch(str(x), '32*54?123'):
#         if '0' not in str(x) and len(str(x))%2==0:
#             s = str(x)
#             if sum(map(int, s[:len(s) // 2]))==sum(map(int, s[len(s) // 2:])):
#                 print(x, x//519)