# for a in range(1, 300):
#     k=0
#     for x in range(1, 10001):
#         for b in range(60, 81):
#             if ((x % a == 0) or ((x % b) <= (x % 22 != 0))) == True:
#                 k += 1
#             else:
#                 break
#     if k == 10000 * 21:
#         print(a)
for a in range (1, 1000):
    can = True
    for x in range (1, 1000):
        if ((x % a == 0) or ((60 <= x <= 80) <= (x % 22 != 0))) == 0:
            can = False
            break
    if can:
        print(a)