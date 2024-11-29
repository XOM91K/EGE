def v5(d):
    s = ''
    while d > 0:
        s = str(d % 5) + s
        d //= 5
    return s

d = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
d = v5(d)
print(d.count('1') + d.count('2') * 2 + d.count('3') * 3 + d.count('4') * 4)
# d = '21309271409123949242934934329420349423472342342795'
# print(d.count('1') + d.count('2') * 2 + d.count('3') * 3 + d.count('4') * 4 + d.count('5') * 5 + d.count('6') * 6 + d.count('7') * 7 + d.count('8') * 8 + d.count('9') * 9)
# print(sum(map(int, d)))