import ipaddress
for mask in range(0, 33):
    net1 = ipaddress.ip_network(f'216.54.187.235/{mask}', 0).hosts()
    net2 = ipaddress.ip_network(f'216.54.174.128/{mask}', 0).hosts()
    if net1 != net2:
        print(mask)