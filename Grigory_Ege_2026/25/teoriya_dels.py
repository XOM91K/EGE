# def dels(d):
#     l = []
#     for x in range(1, d + 1):
#         if d % x == 0:
#             l.append(x)
#     return l
# d = 100_000_000
# # [1, 2, 4, 5....50, 100]
# print(dels(d))
#print(*dels(d))

# def dels(d):
#     l = []
#     for x in range(1, d // 2 + 1):
#         if d % x == 0:
#             l.append(x)
#     l.append(d)
#     return l
# d = 100_000_000_000
# [1, 2, 4, 5....50, 100]
# print(dels(d))

# def dels(d):
#     l = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             l.append(x)
#             l.append(d // x)
#     return sorted(set(l))
# d = 100
# print(dels(d))

d = 1170
# def dels(d):
#     l = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             if x % 2 != 0:
#                 l.append(x)
#             if (d // x) % 2 != 0:
#                 l.append(d // x)
#     return sorted(set(l))
# print(dels(1170))
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
d = 0
print(is_prime(d))