def v5(a):
    s = ''
    while a > 0:
        s += str(a % 5)
        a //= 5
    return s[::-1]
d = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
print(sum(map(int, v5(d))))
#print('2' * 20)