import math
l = [int(x) for x in open('3.txt')]
mx = [x for x in l if x > 350]
mn = [x for x in l if x <= 350]

print(mn)
mx = mx[::-1]
print(mx)
sm = sum(mn)
for x in range(len(mx)):
    if (x + 1) % 3 != 0:
        sm += mx[x]
    else:
        sm += mx[x] * 0.25
print(math.ceil(sm))
# i = 0
# j = len(l) - 1
# ct = 0
# sm = 0
# while ct < len(l):
#     ct += 1
#     if ct % 3 != 0:
#         sm += l[i]
#         i += 1
#     elif l[j] > 350:
#         sm += l[j] * 0.25
#         j -= 1
#     else:
#         sm += l[j]
#         j -= 1
# print(math.ceil(sm))