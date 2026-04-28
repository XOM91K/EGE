# l = [int(x) for x in open('27.txt')]
# l = sorted(l)
# lt = 0
# rt = len(l) - 1
# new_l = []
# ct = 0
# sm = 0
# while lt <= rt:
#     new_l.append(l[lt])
#     sm += l[lt]
#     lt += 1
#     ct += 1
#     if ct % 8 == 0:
#         new_l.append(l[rt])
#         rt -= 1
#         ct = 0
# print(new_l)
# print(sm)
l = [int(x) for x in open('27.txt')]
l = sorted(l)
lt = 0
rt = len(l) - 1
new_l = []
ct = 0
sm = 0
while lt <= rt:
    new_l.append(l[lt])
    sm += l[lt]
    lt += 1
    ct += 1
    if ct % 2 == 0:
        new_l.append(l[rt])
        rt -= 1
        ct = 0
print(new_l)
print(sm)