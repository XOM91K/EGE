import fnmatch
def get_max_min_del(num):
    lst = []
    for x in range(1, int(num ** 0.5) + 1):
        if num % x == 0:
            lst.append(x)
            lst.append(num // x)
    lst.sort()
    return sum([lst[0], lst[-1]])
for x in range(7777, 10 ** 10 + 1, 7777):
    if fnmatch.fnmatch(str(x), '12*567?') and get_max_min_del(x) % 2 != 0:
        print(x, x // 7777)