import ipaddress
for mask in range(17, 33):
    net1 = ipaddress.ip_network(f'200.154.190.12/{mask}', 0)
    net2 = ipaddress.ip_network(f'200.154.184.0/{mask}', 0)
    if net1 == net2:
        print(mask)