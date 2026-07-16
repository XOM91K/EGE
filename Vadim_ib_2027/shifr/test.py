s = 'ABC'
print(list(s.encode()))
print(bytes([65 ^ 5, 66 ^ 5, 67 ^ 5]).decode())
