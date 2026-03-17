def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))


l = [int(d) for d in open('12.txt')]
mx = []
for x in range(len(l) - 1):
    if l[x] % 2 != l[x + 1] % 2:
        dl1 = dels(l[x])
        dl2 = dels(l[x + 1])
        if len(set(dl1).intersection(set(dl2))) == 1:
            mx.append(l[x] + l[x + 1])
print(len(mx), min(mx))

# k = 0
# if is_prime(l[x]):
#     if l[x] % 2 == 0 and l[x + 1] % 2 != 0:
#         k += 1
# if is_prime(l[x + 1]):
#     if l[x + 1] % 2 == 0 and l[x] % 2 != 0:
#         k += 1
# if k == 1:
#     mx.append(l[x] + l[x + 1])
