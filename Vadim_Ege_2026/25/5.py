import fnmatch

# def dels(x):
#     k = []
#     for y in range(2,int(x**0.5)+1):
#         if x%y == 0:
#             k.append(x//y)
#             k.append(y)
#     return sorted(set(k))
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
c=0
for x in range(1,10**7):
    if is_prime(x):
        if fnmatch.fnmatch(str(x),"3?1111*"):
            print(x)