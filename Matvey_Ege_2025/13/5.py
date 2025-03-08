import ipaddress
ip_me = ipaddress.ip_address('92.52.42.52')
for mask in range(25, 33):
        net = ipaddress.ip_network(f'92.52.42.0/{mask}', 0)
        if ip_me in net:
            print(net.netmask)