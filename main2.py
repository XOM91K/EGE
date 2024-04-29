from math import gcd
import itertools

s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
ct = 0
gd = gcd(a, b)
uni = []
def shift_left(s, k):
    n = len(s)
    k = k % n  # учитываем случай, когда k > n
    return s[k:] + s[:k]
def shift_right(s, k):
    n = len(s)
    k = k % n  # учитываем случай, когда k > n
    return s[n - k:] + s[:n - k]
def unique_binary_strings(string):
    for x in range(gd):
        shifted_left = shift_left(string, x)
        shifted_right = shift_right(string, x)
        uni.append(shifted_right)
        uni.append(shifted_left)
for s in itertools.product('01', repeat=gd):
    s = ''.join(s)
    s *= max(a,b,c) * 2
    s_a = set()
    s_b = set()
    s_c = set()
    for x in range(a, len(s), a):
        s_a.add(s[x - 1])
    for y in range(b, len(s), b):
        s_b.add(s[y - 1])
    for z in range(c, len(s), c):
        s_c.add(s[z - 1])
    if len(s_a) == 1 and len(s_b) == 1 and len(s_c) == 2:
        if s[:gd] not in uni:
            ct += 1
        unique_binary_strings(s[:gd])
if gd % c == 0:
    ct = 0
print(ct)
