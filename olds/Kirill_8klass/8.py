import string
alf = '0123456789' + string.ascii_lowercase
print(alf)
def to_k(n, k):
    s = ''
    while n > 0:
        s += str(alf[n % k])
        n //= k
    return s[::-1]
d = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
d = to_k(d, 15)
print(len(set(d)))

# s = 'abracadabra'
# print(set(s))