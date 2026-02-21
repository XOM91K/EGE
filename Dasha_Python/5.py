# l = [33, 10, 22, -56, 77, 3, 2, 10, 5, 9, 22, -50]
# r = []
# for d in l:
#     if d % 3 == 0:
#         r.append(d)
# print(r)
# print([d * 2 for d in l if d % 3 == 0])
# l = list(map(int, input().split()))
# print(l)
# l = [int(d) for d in input().split()]
# print(l)
# l = [int(x) for x in input().split()]
# l.append(l[0] + l[-1])
# l = sorted(l)
# print(*l)
s = 'Apple banana Cherry'.split()
for x in s:
    x = x.replace('A', 'a')
    x = x.replace('a', '@', 1)
    print(x, end=' ')