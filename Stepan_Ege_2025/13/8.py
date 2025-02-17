import ipaddress
ip1 = ipaddress.ip_network('192.168.56.192/255.255.255.192', 0)
ip2 = ipaddress.ip_network('192.168.56.208/255.255.255.240', 0)
print(len(set(ip1).symmetric_difference(set(ip2))))
