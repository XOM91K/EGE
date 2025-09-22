import ipaddress
for mask in range(20, 33):
    net = ipaddress.ip_network(f'92.52.42.0/{mask}', 0)
    ip = ipaddress.ip_address('92.52.42.52')
    if ip in net:
        print(ip, list(net))