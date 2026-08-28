# s = [[int(y) for y in x.split()] for x in open('lambda_.txt')]
# N = 485
# for x in s:
#     x.append(sum(x[1:-1]))
# s = sorted(s, key=lambda d: (-d[-1], -d[-2], d[0]))
# k = 0
# ct = 0
# poluproxod = s[N - 1][-1]
# for x in s:
#     k += 1
#     if x[-1] == poluproxod:
#         ct += 1
#     print(k, x)
# print(ct)