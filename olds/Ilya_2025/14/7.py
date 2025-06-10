d = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
s = ''
while d > 0:
    s += str(d % 5)
    d //= 5
print(sum(map(int, s)))