# O(n)
# def is_prime(d):
#     for x in range(2, int(d ** 0.5) + 1):
#         if d % x == 0:
#             return False
#     return True
# d = 13712937127
# print(is_prime(d))

# def dels(d):
#     l = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             l.append(x)
#             l.append(d // x)
#     return l
# d = 500_000_000
# print(dels(d))