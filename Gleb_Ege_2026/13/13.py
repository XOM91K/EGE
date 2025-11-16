import ipaddress

l = []
d = list(ipaddress.ip_network('192.168.56.192/255.255.255.192', 0))
g = list(ipaddress.ip_network('192.168.56.208/255.255.255.240', 0))
print(len(set(d).symmetric_difference(set(g))))