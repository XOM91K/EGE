from ipaddress import*
k = 0

for a in range(0, 256):
    c = 1
    net = ip_network(f'246.81.65.{a}/255.255.255.224', False)
    for ip in net:
        bom = bin(int(ip))[2:].zfill(32)
        if bom[16:24].count('0') <= bom[24:].count('0'):
            c = 0
    if c == 1:
        k += 1
print(k)