def is_prime(d):
    for i in range(2, int(d ** 0.5) + 1):
        if d % i == 0:
            return False
    return d > 1
for x in range(10 ** 7):
    if is_prime(x):
        if str(x)[0] == '3' and str(x)[2:6] == '1111':
            print(x)
            #3000000