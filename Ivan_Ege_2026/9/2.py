# l = [[int(d) for d in x.split()] for x in open('2.txt')]
# ct = 0
# for x in l:
#     kr3 = [d for d in x if d % 3 == 0]
#     if len(kr3) == 3:
#         if max(x) - min(x) <= sum(kr3):
#             ct += 1
# print(ct)

l = [[int(d) for d in x.split()] for x in open('3.txt')]
for x in l:
    print(x)