import ipaddress
ip1 = ipaddress.IPv4Address('165.112.200.70')
ip1 = ipaddress.ip_network(ip1.exploded + '/32', False)
ip2 = ipaddress.IPv4Address('165.112.175.80')
ip2 = ipaddress.ip_network(ip1.exploded + '/32', False)
print(ip1.netmask)
print(ip2.netmask)