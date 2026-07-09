# def is_prime(d):
#     for x in range(2, int(d ** 0.5) + 1):
#         if d % x == 0:
#             return False
#     return d > 1
# def dels(d):
#     dls = []
#     for x in range(2, int(d ** 0.5) + 1):
#         if d % x == 0:
#             if is_prime(d):
#                 dls.append(x)
#             if is_prime(d // x):
#                 dls.append(d // x)
#         if len(dls) >= 2:
#             break
#     return sorted(set(dls))
# for x in range(8_007_494_155, 10 ** 10):
#     M = dels(x)
#     if len(M) > 0:
#         M = M[0] + M[-1]
#         if M > 80_000 and is_prime(M) and '567' in str(M):
#             print(x)
def f(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i]+f(x//i)
    return [x]

for x in range(8_007_494_155,8_300_000_000):
    d = f(x)
    if len(d)>1:
        M = max(d)+min(d)
        if M>80_000 and str(M).count('567')==1 and len(f(M))==1:
            print(x,M)