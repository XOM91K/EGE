a = [9, 8, 55, 2, 10, 29, 22, 33, 44, 137, 1]
# n = 10
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for x in a:
    if is_prime(x):
        print(x)