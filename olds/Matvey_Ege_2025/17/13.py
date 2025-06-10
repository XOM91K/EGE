# def is_prime(d):
#     for i in range(2, int(d ** 0.5) + 1):
#         if d % i == 0:
#             return False
#     return d > 1
def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))
mn = []
l = [int(x) for x in open('13.txt')]
for x in range(len(l) - 1):
    dls1 = dels(l[x])
    dls2 = dels(l[x + 1])

    if set(dls1).intersection(dls2) == {1}:
        print(dls1, dls2)
        if l[x] % 2 != l[x + 1] % 2:
            mn.append(l[x] + l[x + 1])
print(len(mn), min(mn))
