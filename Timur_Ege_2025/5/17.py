def v3(a):
    s = ''
    while a > 0:
        s += str(a % 3)
        a //= 3
    return s[::-1]
