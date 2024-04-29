# # def g(s, p):
# #     if str(s)[-1] == '0' and p == 2:
# #         return 1
# #     elif str(s)[-1] != '0' and p == 2:
# #         return 0
# #     elif str(s)[-1] == '0':
# #         return 0
# #     if p % 2 == 0:
# #         return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s + 11, p + 1)
# #     else:
# #         return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s + 11, p + 1)
# # for x in range(10, 100):
# #     if x % 10 != 0:
# #         if g(x, 0):
# #             print(x)
# ct = 0
# def g(s, p):
#     if str(s)[-1] == '0' and p == 3:
#         return 1
#     elif str(s)[-1] != '0' and p == 3:
#         return 0
#     elif str(s)[-1] == '0':
#         return 0
#     if p % 2 != 0:
#         return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s + 11, p + 1)
#     else:
#         return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s + 11, p + 1)
# for x in range(10, 100):
#     if x % 10 != 0:
#         if g(x, 0):
#             ct += 1
#             print(x, ct)
z = []
def g(s, p):
    if str(s)[-1] == '0' and (p == 2 or p == 4):
        return 1
    elif str(s)[-1] != '0' and p == 4:
        return 0
    elif str(s)[-1] == '0':
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s + 11, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s + 11, p + 1)
for x in range(10, 100):
    if x % 10 != 0:
        if g(x, 0):
            z.append(x)
            print(x)
print(sum(z) - 504)