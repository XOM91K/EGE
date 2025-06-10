import ipaddress
for net in range(0, 33):
    for net2 in range(0, 33):
        ip1 = ipaddress.ip_network(f'151.172.115.121/{net}', 0)
        ip2 = ipaddress.ip_network(f'151.172.115.156/{net2}', 0)
        if ip1 != ip2:
            if net == net2:
                print(net)
