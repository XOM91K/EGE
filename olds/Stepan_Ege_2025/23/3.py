def f(x, y, s):
    if x > y or 'CA' in s:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 2, y, s + 'A') + f(x + 3, y, s + 'B') + f(x * 4, y, s + 'C')
print(f(1, 50, ''))
# 1 - 50
# ACBABCABBCBCACBABCABABCABCBCABCABACBABCABCABCB