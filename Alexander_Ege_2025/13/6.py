import ipaddress
for mask in range(0, 33):
    net = ipaddress.ip_network('92.52.42.0/' + str(mask), 0)
    ip = ipaddress.ip_address('92.52.42.52')
    if ip in net:
        print(net.netmask)