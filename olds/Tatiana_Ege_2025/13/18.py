import ipaddress
for mask in range(16, 33):
    net1 = ipaddress.ip_network(f'126.115.78.15/{mask}', 0)
    net2 = ipaddress.ip_network(f'126.115.84.26/{mask}', 0)
    if net1 == net2:
        k = 0
        for ip in net1:
            ip = bin(int(ip))[2:].zfill(32)
            if ip.count('1') == 22:
                k += 1
        print(k)