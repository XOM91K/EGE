l = [int(x) for x in open('1.txt')]
N = min([x for x in l if x % 15 != 0])
mx = []
for i in range(len(l) - 1):
    # l[i]  l[i + 1]
    if l[i] % N == 0 and l[i + 1] % N == 0:
        mx.append(l[i] + l[i + 1])
print(len(mx), max(mx))
# l = [1, 100, -59, 13, 14, 19]
# print([x for x in l if x % 2 != 0])
# r = []
# for x in l:
#     if x % 2 != 0:
#         r.append(x)
# print(r)