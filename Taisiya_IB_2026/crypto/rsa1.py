import sympy
from Crypto.Util.number import long_to_bytes, bytes_to_long
c = 408114776764409099690169640113227
n = 2347332715134999472660100244460421
e = 65537 # открытый ключ
p, q = sympy.factorint(n)
fi = (p - 1) * (q - 1)
d = pow(e, -1, fi) # приватный ключ
print('d:', d)
m = pow(c, d, n)
print(p, q)
print(long_to_bytes(m))
print(bytes_to_long('c0mm4nd_bl0ck5'.encode()))