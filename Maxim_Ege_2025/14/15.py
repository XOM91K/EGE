for x in range(1,1000000):
    a = 3**200 + 3**10 - x
    b = ''
    while a > 0:
        b += str(a%3)
        a //= 3
    h = b[::-1]
    if h.count('2') == 200:
        print(x,h)