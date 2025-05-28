import ipaddress
for mask in range(0, 33):
    net1 = ipaddress.ip_network(f'120.91.85.213/{mask}', 0)
    net2 = ipaddress.ip_network(f'120.91.89.205/{mask}', 0)
    if net1 == net2:
        print(net1.netmask)