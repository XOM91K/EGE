import ipaddress
for net in range(33):
    network = ipaddress.ip_network(f'205.154.192.0/{net}', 0)
    if ipaddress.ip_address('205.154.212.20') in network:
        print(network.netmask)