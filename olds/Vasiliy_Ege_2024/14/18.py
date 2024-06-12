def v5(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n = n //5
    return s[::-1]
c = v5((5**2004)- (5**1016)-(25**508)-(5**400)+(25**250)-27)
print(c.count('4'))