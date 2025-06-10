
def v5(d):
    s = ''
    while d > 5:
        s= str(d % 5) + s
        d //= 5
    return s
for x in range(3, 2025):
    d = 5**2025 + 5**200 - x
    d = v5(d)
    if d.count('4') > 198:
        print(x, d.count('4'))