# for x in range(1, 255):
#     s = '68656c6c6f7f637466'
#     d = list(bytes.fromhex(s))
#     a = ''
#     for y in d:
#         a += chr(y ^ x)
#     print(a, x)
import base64
print(base64.b64encode('данные'.encode()))