import ipaddress
for mask in range(15, 33):
    net1 = ipaddress.ip_network(f'75.32.145.15/{mask}', 0)
    net2 = ipaddress.ip_network(f'75.32.136.235/{mask}', 0)
    ct = 0
    if net1 == net2:
        for ip in net1.hosts():
            ip = bin(int(ip))[2:].zfill(32)
            if ip.count('1') % 2 == 0:
                ct += 1
        print(mask, ct)