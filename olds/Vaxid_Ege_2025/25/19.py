# import fnmatch
# for x in range(27919, 10 ** 14, 27919):
#     if fnmatch.fnmatch(str(x), '125???125**554'):
#         print(x, x // 27919)
import itertools
for x in range(10):
    for y in range(10):
        for z in range(10):
            comb = itertools.product('0123456789', repeat=2)
            for w in comb:
                w = ''.join(w)
                c = '125' + str(x) + str(y) + str(z) + '125' + str(w) + '554'
                if int(c) % 27919 == 0 and int(c) < 10 ** 14:
                    print(c, int(c) // 27919)