import ipaddress
ct = 0
l1 = set()
l2 = set()
for x in ipaddress.ip_network('192.168.56.192/255.255.255.192', False):
    x = bin(int(x))[2:]
    l1.add(x)
for x in ipaddress.ip_network('192.168.56.208/255.255.255.240', False):
    x = bin(int(x))[2:]
    l2.add(x)
print(len(l1.difference(l2)))
