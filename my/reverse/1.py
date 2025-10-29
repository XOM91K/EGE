s = '\x03BG\x04EhD\x04TE\x04ChG\x03DD@\aES'
print(len(s))
for x in s:
    print(chr(ord(x) ^ 0x37), end='')