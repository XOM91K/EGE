a = [9, 8, 551231231234, 2123123131, 10,2_147_483_647, 29, 22, 33, 44, 137, 1]
# n = 10
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
for x in a:
    if is_prime(x):
        print(x)