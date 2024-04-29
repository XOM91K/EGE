def prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
def min_del_prime(n):
    mins = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0 and prime(x):
            mins.append(x)
        if n % (n // x) == 0 and prime(n // x):
            mins.append(n // x)
    return mins
ct = 0
for x in range(121332132, 20222022 - 1, -1):
    if len(min_del_prime(x)) != 0 and min_del_prime(x)[0] > 999:
        print(x, min_del_prime(x))
        ct += 1
    if ct == 5 :
        break