import ipaddress
ct = 0
k = 0
net1 = ipaddress.ip_network("192.168.56.192/255.255.255.192", 0)
net2 = ipaddress.ip_network("192.168.56.208/255.255.255.240", 0)
print(len(set(net1) & set(net2)))
print(len(set(net1) | set(net2)))