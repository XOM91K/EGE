import ipaddress
for mask in range(0, 33):
    net1 = ipaddress.ip_network(f'121.171.5.70/{mask}', 0)
    net2 = ipaddress.ip_network(f'121.171.5.107/{mask}', 0)
    if net1 == net2:
        print(mask)