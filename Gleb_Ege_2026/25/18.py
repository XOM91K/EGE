def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def stepen(d):
    for x in range(2, 3000):
        if is_prime(x):
            for y in range(2, 20):
                if x ** y == d:
                    return x
    return -1
for x in range(700001, 10 ** 6):
    r = stepen(x)
    if r != -1:
        print(x, r)