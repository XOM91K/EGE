import ipaddress
for mask in range(0, 33):
    net = ipaddress.ip_network(f'212.145.124.210/{mask}', 0)
    if str(net) == f'212.145.124.0/{mask}':
        print(mask)