import ipaddress
for mask in range(0,33):
    net=ipaddress.ip_network(f'120.91.176.213/{mask}',0)
    net2=ipaddress.ip_network(f'120.91.174.205/{mask}', 0)
    if net == net2:
        print(net.netmask)