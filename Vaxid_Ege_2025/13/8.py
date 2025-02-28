import ipaddress
for mask in range(16, 33):
    ip_net1 = ipaddress.ip_network(f'176.213.225.119/{mask}', False)
    ip_net2 = ipaddress.ip_network(f'176.213.195.58/{mask}', False)
    if ip_net1 == ip_net2:
        print(ip_net1.netmask)