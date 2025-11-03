# def dels(d):
#     l = []
#     for x in range(2, int(d ** 0.5) + 1):
#         if d % x == 0:
#             l.append(x)
#             l.append(d // x)
#     return sorted(set(l))
# d = 100
# print(dels(d))
def is_prime(r):
    for x in range(2, int(r ** 0.5) + 1):
        if r % x == 0:
            return False
    return r > 1
d = 0
print(is_prime(d))
