#
# def dels(d):
#     l = []
#     c = 2
#     while c * c <= d:
#         while d % c == 0:
#             l.append(c)
#             d //= c
#         c += 1
#     if d > 1:
#         l.append(d)
#     return l
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) and x % 2 != 0:
                dls.append(x)
            if is_prime(d // x) and x % 2 != 0:
                dls.append(d // x)
    return sorted(set(dls))
for x in range(5_000_001, 10 ** 7):
    mns = dels(x)
    if len(mns) >= 2:
        # if len(mns) == 2:
        #     if is_prime(mns[0] * mns[1]):
        #         print(x, max(mns))
        # elif len(mns) == 3:
        #     if is_prime(mns[0] * mns[1]) or is_prime(mns[1] * mns[2]) or is_prime(mns[0] * mns[2]):
        #         print(x, max(mns))
        if is_prime(abs(mns[0] - mns[-1])) and mns[0] * mns[-1] == x:
            print(x, max(mns))