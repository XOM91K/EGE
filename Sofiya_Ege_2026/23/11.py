import functools

l = []


@functools.lru_cache(None)
def f(x, k, flag):
    print(len(set(l)))
    if x == 17:
        flag = 1
    if k > 8 or (k == 8 and flag == 0):
        return 0
    if k == 8 and flag == 1:
        l.append(x)
    return f(x + 8, k + 1, flag) + f(x - 6, k + 1, flag)


print(f(7, 0, 0))
