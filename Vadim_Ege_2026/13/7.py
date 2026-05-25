import ipaddress
ct = 0
for A in range(0, 256):
    for ip in ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', 0).hosts():
        ip = bin(int(ip))[2:].zfill(32)
        if ip[-16:-8].count('0') <= ip[-8:].count('0'):
            print(ip, ip[-16:-8], ip[-8:])
            break
    else:
        ct += 1
print(ct)