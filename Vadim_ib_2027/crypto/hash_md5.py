# import hashlib
# s = open('words.txt').readlines()
# for x in s:
#     x = x.strip()
#     if hashlib.md5(x.encode()).hexdigest() == '26cd8359360bb9bb58373ba531edab0c':
#         print(x)
import base64
print(base64.b64decode('U2FsdGVkX1+rsaQSRL76tRJH8JTaDSzlmBK0W5sUUE5ZJCJ38Nf5j0rUauH2a1RW'))