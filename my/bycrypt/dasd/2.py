flag = '81fcc34beea7e165a77b72cb28a13fff66d6628d9e3987c908c19061614055c54ac5e99d5e83c9eda7cac08ef09894cc'
# C = A * P + B  mod 2**64
# 00 => b64239b67aee271c => C = B = b64239b67aee271c
B = 'b64239b67aee271c'
C2 = int.from_bytes(bytes.fromhex('2fe0984a57a09f24'), 'little')
# 01 => C = A + B => A = C - B = 2fe0984a57a09f24 - b64239b67aee271c
B = int.from_bytes(bytes.fromhex(B), 'little')
A = C2 - B
# P = (C - B) * A^(-1)  mod 2**64
flag = int.from_bytes(bytes.fromhex(flag)[:8][::-1])
P = ((flag - B) * pow(A, -1, 2 ** 64)) % 2 ** 64
from Crypto.Util.number import long_to_bytes
print(long_to_bytes(P))