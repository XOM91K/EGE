import ipaddress
ct = 0
for a in range(0, 256):
    can = True
    for x in list(ipaddress.ip_network(f'246.81.65.{a}/255.255.255.224', 0))[1:-1]:
        x = bin(int(x))[2:].zfill(32)
        if x[16:-8].count('0') <= x[-8:].count('0'):
            can = False
    if can:
        ct += 1
print(ct)