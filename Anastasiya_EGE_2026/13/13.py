import ipaddress
ct = 0
for A in range(0, 256):
    net = ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', 0).hosts()
    can = True
    for ip in net:
        ip = bin(int(ip))[2:].zfill(32)
        if ip[16:24].count('0') <= ip[-8:].count('0'):
            can = False
    if can:
        print(A)
        ct += 1
print(ct)