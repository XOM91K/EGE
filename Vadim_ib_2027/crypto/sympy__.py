import Crypto.Util.number
p = 4722366482869645218097
q = 4722366482869645253047
e = 65537
c = 9591060199519757108428617152343061202521210

# from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
# p, q = sorted(sympy.factorint(2347332715134999472660100244460421))
# e = 65537
# fi = (p - 1) * (q - 1)
# n = 2347332715134999472660100244460421
# d = pow(e, -1, fi)
# c = 408114776764409099690169640113227
# m = pow(c, d, n)
# print(long_to_bytes(m).decode())