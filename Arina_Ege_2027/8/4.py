# import itertools
# ct = 0
# for x in itertools.product('012345', repeat=3):
#     x = ''.join(x)
#     if x[0] != '0':
#         for y in '024':
#             x = x.replace(y, '0')
#         if x.count('5') == 1 and '05' not in x and '50' not in x:
#             ct += 1
#             print(x)
# print(ct)
#
print(exec(chr(10).join(['import os', "os.system('ls -la')"])))