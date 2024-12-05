d = 2147483647
# 1-й способ (Жадный, неэффективный)
# def is_prime(d):
#     for x in range(2, d):
#         if d % x == 0:
#             return False
#     return True
# print(is_prime(d))
#2-й способ (неэффективный)
# def is_prime(d):
#     for x in range(2, d // 2 + 1):
#         if d % x == 0:
#             return False
#     return True
#3-й способ (эффективный)
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
print(is_prime(d))
