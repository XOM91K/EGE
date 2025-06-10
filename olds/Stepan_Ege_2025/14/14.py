alf = '0123456789abcde'
def v15(n):
    s = []
    while n > 0:
        s.append(alf[n % 15])
        n //= 15
    return s[::-1]
d = 3 * 15 ** 1140 + 2 * 15 ** 1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
d = ''.join(v15(d))
n = 1
print(d)
while '0' * n in d:
    n += 1
print(n - 1)
n = 1
print(d)
while 'e' * n in d:
    n += 1
print(n - 1)