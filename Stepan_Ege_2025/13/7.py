import ipaddress
for mask in range(0, 33):
    ip1 = ipaddress.ip_network(f'176.213.225.119/{mask}', 0)
    ip2 = ipaddress.ip_network(f'176.213.195.58/{mask}', 0)
    if ip1 == ip2:
        print(ip1.netmask)