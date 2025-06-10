import ipaddress
ct = 0
ip_net1 = ipaddress.ip_network('192.168.56.192/255.255.255.192', False)
ip_net2 = ipaddress.ip_network('192.168.56.208/255.255.255.240', False)
s1 = set(list(ip_net1))
s2 = set(list(ip_net2))
print(s1)
print(s2)
print(len(s1.symmetric_difference(s2)))