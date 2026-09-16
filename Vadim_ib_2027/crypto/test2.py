import sympy
from Crypto.Util.number import long_to_bytes
n = 4951760159909264545859816971
e = 65537
c = 2327009866379170405741779145
p, q = sympy.factorint(n)
fi = (p - 1) * (q - 1)
d = pow(e, -1, fi)
m = pow(c, d, n)
print(long_to_bytes(m).decode())