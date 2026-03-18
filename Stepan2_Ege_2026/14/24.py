def v9(d):
    s = ''
    while d > 0:
        s = str(d % 9) + s
        d //= 9
    return s
d = 19 ** 81 + 23 ** 709 - 4
d = v9(d)
print(d.count('81') + d.count('82') + d.count('83') + d.count('84') + d.count('85') + d.count('86') + d.count('87'))