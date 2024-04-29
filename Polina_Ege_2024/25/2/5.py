def prime(n):
    if n == 1:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
k = 0
for x in range(5962464, 5962582):
    if prime(x):
        k += 1
        print(k, x)