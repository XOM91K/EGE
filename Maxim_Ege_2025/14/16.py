for x in range(1,10000):
    a = 6**900 + 6**10 - x
    b = ''
    while a > 0:
        b += str(a%6)
        a //= 6
    if b.count('3') == b.count('5'):
        print(x)