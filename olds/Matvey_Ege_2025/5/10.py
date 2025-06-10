# def v8(n):
#     c = ''
#     while n > 0:
#         c += str(n % 8)
#         n //= 8
#     return c[::-1]
for n in range(1, 10000):
    r = oct(n)[2:]
    if n % 2 == 0:
        r += oct(max(map(int, r)))[2:]
    else:
        r += oct(min(map(int, r)) * 2)[2:]
    if int(r, 8) < 313:
        print(n)
