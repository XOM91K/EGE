import ipaddress
for mask in range(15, 33):
    net1 = ipaddress.ip_network(f'192.169.170.31/{mask}', 0)
    net2 = ipaddress.ip_network(f'192.169.170.21/{mask}', 0)
    if net1 == net2:
        print(mask, len(list(net1)))