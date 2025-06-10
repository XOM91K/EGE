import ipaddress
for net in range(0, 33):
    network = ipaddress.ip_network(f'205.154.192.0/{net}', 0)
    ip = ipaddress.ip_address('205.154.212.20')
    if ip in network:
        print(network.netmask)
