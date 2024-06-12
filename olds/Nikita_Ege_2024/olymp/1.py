from math import gcd
s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = (2 ** gcd(a, b) // c) - (gcd(a, b) - 1)
if gcd(a, b) % c == 0:
    d = 0
print(d)