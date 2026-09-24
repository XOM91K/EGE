import ipaddress
for x in ipaddress.ip_network('95.24.30.144/255.255.248.0', 0):
    print(x)