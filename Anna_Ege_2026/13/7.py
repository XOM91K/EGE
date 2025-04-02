import ipaddress
for mask in range(0, 33):
    net1 = ipaddress.ip_network(f'176.213.225.119/{mask}',0)
    net2 = ipaddress.ip_network(f'176.213.195.58/{mask}', 0)
    if net1 == net2:
        print(net2.netmask)