# for x in range(1, 10000):
#     try:
#         f = open(f'{x}.txt').readline()
#         print(5 / 0)
#         if f.startswith('vsosh'):
#             print(f)
#     except FileNotFoundError:
#         pass
#     except ZeroDivisionError:
#         print('Деление на ноль нельзя')
import collections
d = ['hello', 'hello', 'world', 'world']
sl = {}
for x in d:
    if x not in sl:
        sl[x] = 0
    sl[x] += 1
print(sl)
# print(dict(collections.Counter(d)))