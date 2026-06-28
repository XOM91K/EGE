# l = [5, 9, -2, 4, 9]
# for x in l:
#     print(l.index(x))
# s = 'abracadabra'
# print(s[::-2])
# print(s)
# print(s[:2])
# print(s[-4:])
# l = [5, 10, -5, 3, 1]
# # l.sort()
# print(sorted(l))
# print(l)
# d = '1;2;3;4'.split(';')
# print(tuple(map(int, d)))
# l = [x for x in range(1, 1_000_001)]
# t = (x for x in range(1, 1_000_001))
# print(l.__sizeof__())
# print(t.__sizeof__())
a = {1, 2, 3}
b = {4, 5, 6, 3}
print(a.intersection(b), a & b)
print(a.union(b), a | b)
print(a.difference(b), a - b)
print(a.symmetric_difference(b))