# import sympy
# from Crypto.Util.number import long_to_bytes
# c = 408114776764409099690169640113227
# p, q = sympy.factorint(2347332715134999472660100244460421)
# n = 2347332715134999472660100244460421
# fi = (p - 1) * (q - 1)
# e = 65537
# d = pow(e, -1, fi)
# m = pow(c, d, n)
# print(long_to_bytes(m))
# print(long_to_bytes(5723662165843207754))
flag = [240, 245, 233, 245, 238, 253, 239, 217, 234, 182, 240, 181, 217, 229, 244, 255, 246, 242, 182, 217, 242, 238, 183, 232, 225, 179, 251]
for y in flag:
    print(chr(y ^ 134), end ='')