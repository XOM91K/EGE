import ipaddress
for x in range(33):
    ip1 = ipaddress.ip_network(f'176.213.225.119/{x}', 0)
    ip2 = ipaddress.ip_network(f'176.213.195.58/{x}', 0)
    if ip1 == ip2:
        print(ip1.netmask)
# print(bin(int(ipaddress.ip_address('255.255.255.240')))[2:])
# print(d)