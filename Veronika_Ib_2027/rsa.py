import sympy
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
n = 4951760159909264545859816971
e = 65537
c = 2327009866379170405741779145
p, q = sympy.factorint(n)
fn = (p - 1) * (q - 1)
d = pow(e, -1, fn)
m = pow(c, d, n)
print(long_to_bytes(m))