import ipaddress
for mask in range(0, 33):
    net = ipaddress.ip_network('92.52.42.52/' + str(mask), 0)
    print(net, net.netmask)
# net = ipaddress.ip_network('92.52.42.52/92.52.42.0', 0)
# print(net)