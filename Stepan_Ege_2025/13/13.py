import ipaddress
for mask in range(0, 33):
    net1 = ipaddress.ip_network('120.91.176.213/' + str(mask), 0)
    net2 = ipaddress.ip_network('120.91.174.205/' + str(mask), 0)
    if net1 == net2:
        print(net1.netmask)