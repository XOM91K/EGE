import ipaddress
for mask in range(0, 33):
    network = ipaddress.ip_network(f'92.52.42.52/{mask}', 0)
    print(network, network.netmask)