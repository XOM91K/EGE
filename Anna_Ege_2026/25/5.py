import fnmatch
def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return n > 1
for x in range(2627, 10 ** 9, 2627):
    if is_prime(sum(map(int, str(x)))) and fnmatch.fnmatch(str(x), '7*53?3*1'):
        print(x, x // 2627)