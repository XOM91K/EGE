# n = 3697521940027
# e = 65537
# ct = [191240264626, 2125050717843, 2189163487386, 328696557488, 2388858658013, 1320002161081, 3346372194395, 3279910505075, 1390741397367]
# import sympy
# from Crypto.Util.number import long_to_bytes
# p, q = sorted(sympy.factorint(n))
# print(p, q)
# fi = (p - 1) * (q - 1)
# d = pow(e, -1, fi)
# for c in ct:
#     print(long_to_bytes(pow(c, d, n)).decode(),end='')