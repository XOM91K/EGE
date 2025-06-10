# def is_prime(d):
#     for x in range(2, int(d ** 0.5) + 1):
#         if d % x == 0:
#             return False
#     return d > 1
# def dels(d):
#     dls = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             if is_prime(x) and str(x).count('0') == 1 and is_prime(d // x ) and str(d // x).count('0') == 1:
#                 dls.append(x)
#                 dls.append(d // x)
#     return sorted(set(dls))
# ct = 0
# for x in range(2_900_001, 10 ** 10):
#     f = dels(x)
#     if len(f) >= 2:
#         print(x, max(f))
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) and str(x).count('0') == 1:
                dls.append(x)
            if is_prime(d // x ) and str(d // x).count('0') == 1:
                dls.append(d // x)
    return sorted(set(dls))
ct = 0
for x in range(2_900_001, 10 ** 10):
    f = dels(x)
    if len(f) == 2:
        print(x, max(f))