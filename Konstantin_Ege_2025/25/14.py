import fnmatch
def is_prime(d):
    for q in range(2, d):
        if d % q == 0:
            return False
    return d > 1

for x in range(2627, 10 ** 9, 2627):
    if is_prime(sum(map(int, str(x)))):
        if fnmatch.fnmatch(str(x), '7*53?3*1'):
            print(x, x // 2627)