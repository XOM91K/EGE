import ipaddress
net = ipaddress.ip_network('69.121.128.142/255.255.252.0', 0)
#print(net)
#print(list(net))
for x in net:
    print(x)