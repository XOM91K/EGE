import ipaddress
for mask in range(0, 33):
    ip = ipaddress.ip_address('92.52.42.52')
    net = ipaddress.ip_network(f'92.52.42.0/{mask}', 0)
    if ip in net:
        print(net.netmask)