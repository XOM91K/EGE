e = 19 ** 81 + 23 ** 709 - 4
d = ''
while e > 0:
    d += str(e % 9)
    e //= 9
d = d[::-1]
print(d.count('81') + d.count('82') + d.count('83') + d.count('84') + d.count('85') + d.count('86') + d.count('87'))