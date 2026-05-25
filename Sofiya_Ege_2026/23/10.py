import functools
@functools.lru_cache(None)
def f(x, y, ct, flag):
    if x == 60:
        flag = 1
    if x > y or str(x)[-1] == '3' or '--' in ct:
        return 0
    if x == y and flag == 1:
        return 1
    if x == y and flag == 0:
        return 0
    if x < y:
        return f(x - 1, y, ct + '-', flag) + f(x - 5, y, ct + '-', flag) + f(x + 7, y, ct + '+', flag) + f(x * 2, y, ct + '*', flag)
print(f(9, 84, '', 0))