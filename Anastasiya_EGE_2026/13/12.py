import ipaddress
for mask in range(10, 33):
    net1 = ipaddress.ip_network(f'95.24.2.9/{mask}', 0)
    net2 = ipaddress.ip_network(f'95.24.3.10/{mask}', 0)
    if net1 != net2:
        ct1 = 0
        for ip1 in net1.hosts():
            ip1 = bin(int(ip1))[2:].zfill(32)
            if ip1[-1] == '0':
                ct1 += 1
        ct2 = 0
        for ip2 in net2.hosts():
            ip2 = bin(int(ip2))[2:].zfill(32)
            if ip2[-1] == '0':
                ct2 += 1
        print(mask, max(ct1, ct2))