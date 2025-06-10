import re
d = 53 ** 123 + 65 ** 2222 - 172 ** 12
s = ''
while d > 0:
    s = str(d % 7) + s
    d //= 7
m = re.findall(r'6[1-5]', s)
print(len(m))
