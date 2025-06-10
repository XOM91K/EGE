import ipaddress
for mask in range(0, 33):
    net1 = ipaddress.ip_network(f'3.120.77.205/{mask}', 0)
    net2 = ipaddress.ip_network(f'3.120.77.131/{mask}', 0)
    if net1 != net2:
        print(net1.netmask)