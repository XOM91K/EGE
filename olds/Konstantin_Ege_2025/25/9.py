ct = 0
def is_prime(d):
    for q in range(2, d):
        if d % q == 0:
            return False
    return d > 1
for x in range(2422000, 2422081):
    if is_prime(x):
        ct += 1
        print(ct, x)




# for x in range(2, 2422001):
#     if 2422001 % x == 0:
#         print(x)