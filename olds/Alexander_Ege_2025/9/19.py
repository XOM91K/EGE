# import math
#
# ct = 0
# l = [sorted([int(d) for d in x.split()]) for x in open("992.txt")]
# for x in l:
#     if len(set(x)) < 7:
#         povt = [i for i in x if x.count(i) > 1]
#         nepovt = [i for i in x if x.count(i) == 1]
#         if 3 * sum(nepovt) <= math.prod(povt):
#             ct += 1
# print(ct)
# import math
# s = '1238123129126'
# print(sum(map(int, str(s))))
# #1
# print([int(x) for x in s])
# #2
# print(list(map(int, s)))
# print(math.prod([4, 9, 2]))