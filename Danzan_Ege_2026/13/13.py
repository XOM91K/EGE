import ipaddress
ct = 0
s1 = set()
s2 = set()
for x in ipaddress.ip_network('192.168.56.192/255.255.255.192', 0):
    s1.add(x)
for y in ipaddress.ip_network('192.168.56.208/255.255.255.240', 0):
    s2.add(y)
print(len(s1.symmetric_difference(s2)))