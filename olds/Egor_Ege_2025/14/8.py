a = 53**123 + 65**2222 - 172**12
b = ''
while a > 0:
    b += str(a % 7)
    a //= 7
b = b[::-1]
print(b)
print(b.count("61") + b.count("62") + b.count("63") + b.count("64") + b.count("65"))