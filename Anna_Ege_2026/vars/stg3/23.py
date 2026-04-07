def f(x, y, flag):
    if x == 14 or x == 18:
        flag = 1
    if x > y or x == 17 or x == 28:
        return 0
    if x == y and flag == 1:
        return 1
    if x == y and flag == 0:
        return 0
    if x < y:
        return f(x + 2, y, flag) + f(x + 3, y, flag) + f(x * 2, y, flag)
print(f(8, 48, 0))
# print(f(8, 14) * f(14, 48)) # 1824
# print(f(8, 18) * f(18, 48))  # 6732
# print(f(8, 14) * f(14, 18) * f(18, 48)) # 2244
# print(1824+6732+2244)