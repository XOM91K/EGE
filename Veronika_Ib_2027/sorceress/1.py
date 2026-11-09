import urllib.parse, base64
# print(urllib.parse.unquote('PL%7F_VXc%5DQ%7DcLof%7C%03%7C%5B%7BCVX%7BYVXcO%7C%5B%05%08'))
# #PL%7F_VXc%5DQ%7DcLof%7C%03%7C%5B%7BCVX%7BYVXcO%7C%5B%05%08
# for x in range(1, 256):
#     print(x)
#     for y in b'PL_VXc]Q}cLof||[{CVX{YVXcO|[':
#         print(chr(x ^ y), end='')
#     print()
s = '{"creature":"sorceress"}'
s = base64.b64encode(s.encode())
r = []
for x in s:
    r.append(x ^ 53)
r = bytes(r)
print(urllib.parse.quote(r.decode()))
print(urllib.parse.quote(r))
