# def dels(d):
#     l = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             l.append(x)
#             l.append(d // x)
#     return sorted(set(l))
# d = 100
# l = dels(d)
# print(l)
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
d = 2
print(is_prime(d))