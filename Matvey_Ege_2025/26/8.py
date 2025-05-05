# l = [[int(d) for d in x.split()] for x in open('8.txt')]
# l = sorted(l)
# sl = {}
# ids = []
# for x in l:
#     if x[0] not in sl:
#         sl[x[0]] = []
#     sl[x[0]].append(x[1])
# mx_ct = 0
# for x in sl:
#     sl[x] = sorted(set(sl[x]))
#     ct = 1
#     for y in range(len(sl[x]) - 1):
#         if sl[x][y + 1] - sl[x][y] == 2:
#             ct += 1
#             if ct == 26:
#                 ids.append(x)
#             mx_ct = max(mx_ct, ct)
#         else:
#             ct = 1
# print(mx_ct, min(ids))


sl = {5: 553, 'Hello': 23, 12: -120}
sl[1] = []
sl[1].append(5)
print(sl)
# l = [1, 2, 3]
# print(l[1])
# print(sl)
# print(sl['Hello'])
# print(sl[12])