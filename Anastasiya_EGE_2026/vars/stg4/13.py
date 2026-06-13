import ipaddress
for mask in range(0, 33):
    net = ipaddress.ip_network(f'212.145.124.210/{mask}', 0)
    ip_net = ipaddress.ip_address('212.145.124.0')
    if net == ip_net:
        print(mask)