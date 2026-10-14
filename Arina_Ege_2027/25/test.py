# def is_prime(d):
#     for x in range(2, int(d ** 0.5) + 1):
#         if d % x == 0:
#             return False
#     return d > 1
# # 1 2 4 5 10 20 25 50 100
# def dels(d):
#     l = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             l.append(x)
#             l.append(d // x)
#     return sorted(set(l))
#
# print(is_prime(2_147_483_647))
# print(dels(2_147_483_640))
def mn(d):
    l = []
    c = 2
    while c * c <= d:
        while d % c == 0:
            l.append(c)
            d //= c
        c += 1
    if d > 1:
        l.append(d)
    return l
print(mn(2_147_483_640))
# 2 2 5 5