import ipaddress
for mask in range(10, 33):
    net1 = ipaddress.ip_network(f'211.188.211.49/{mask}', 0)
    net2 = ipaddress.ip_network(f'211.188.200.115/{mask}', 0)
    if net1 == net2:
        print(len(list(net1)))