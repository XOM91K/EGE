from Crypto.Util.number import long_to_bytes
c = 'a2fcc753ffe99af8bd8d311cd5906da41318efb14165b9113c38c93cbd37fdd94c163316f29219729225f47545716d4b'
p1 = '0197d17c39d0a15c' # 00
p2 = '2c2af60ac97d4d7f' # 01
# c = (a * p) + b  mod 2 ** 64
b = int.from_bytes(bytes.fromhex(p1), 'little')
p2 = int.from_bytes(bytes.fromhex(p2), 'little')
a = p2 - b
c = bytes.fromhex(c)
for x in range(0, len(c), 8):
    block = int.from_bytes(c[x: x + 8], 'little')
    p = ((block - b) * pow(a, -1, 2 ** 64)) % 2 ** 64
    p = long_to_bytes(p).decode()[::-1]
    print(p,end='')
# a = p2 - b