# def dels(d):
#     dls = []
#     for x in range(1, d + 1):
#         if d % x == 0:
#             dls.append(x)
#     return dls
def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))
# def dels(d):
#     dls = []
#     for x in range(1, int(d ** 0.5) + 1):
#         if d % x == 0:
#             if x % 2 == 0:
#                 dls.append(x)
#             if (d // x) % 2 == 0:
#                 dls.append(d // x)
#     return dls
d = 144
print(dels(d))