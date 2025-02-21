import ipaddress
for mask in range(0, 33):
    ip_net = ipaddress.ip_network(f'92.52.42.0/{mask}', 0)
    ip_uzel = ipaddress.ip_address('92.52.42.52')
    if ip_uzel in ip_net:
        print(ip_net.netmask)