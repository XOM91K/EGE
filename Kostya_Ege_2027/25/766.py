import fnmatch     # file name match
for x in range(1917, 10 ** 10, 1917):
    if fnmatch.fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)
# for x in range(1917, 10 ** 10 + 1, 1917):
#         s = str(x)
#         if s[0] == '3' and s[2:4] == '12' and s[5:7] == '14' and s[-1] == '5':
#             print(x, x // 1917)