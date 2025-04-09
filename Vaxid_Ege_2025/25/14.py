#*****************
def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return n > 1
def M(n):
    mx_del = [0]
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if is_prime(x):
                mx_del.append(x)
            if is_prime(n // x):
                mx_del.append(n // x)
    return max(mx_del)
ct = 0
for x in range(1_750_001, 10 ** 10):
    MM = M(x)
    if MM <= 15000 and str(MM)[-1] == '7':
        print(x)
        ct += 1
        if ct == 5:
            break