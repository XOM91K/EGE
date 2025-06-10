import ipaddress
for mask in range(0, 33):
    ip1 = ipaddress.ip_network(f'120.91.85.213/{mask}', 0)
    ip2 = ipaddress.ip_network(f'120.91.89.205/{mask}', 0)
    if ip1 == ip2:
        print(ip1.netmask)