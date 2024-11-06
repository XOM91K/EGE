# import itertools
# alf = '0123456789ab'
# ct = 0
# print(alf.index('b'))
# for x in itertools.product(alf, repeat=7):
#     x = ''.join(x)
#     if x.count('b') == 2 and x[0] != '0':
#         x = x.replace('2', '0')
#         x = x.replace('4', '0')
#         x = x.replace('6', '0')
#         x = x.replace('8', '0')
#         x = x.replace('a', '0')
#         x = x.replace('3', '1')
#         x = x.replace('5', '1')
#         x = x.replace('7', '1')
#         x = x.replace('9', '1')
#         x = x.replace('b', '1')
#         if '11' not in x and '00' not in x:
#             ct += 1
# print(ct)