def v25(n):
    c = []
    while n > 0:
        c.append(n%25)
        n//=25
    return c[::-1]
a = v25(15625**16 - 3125**3 * 25**19 + 625**4 - 2005)
print(a.count(0))