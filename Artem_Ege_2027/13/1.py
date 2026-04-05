import ipaddress
for x in ipaddress.ip_network('167.89.100.150/255.255.248.0', 0):
    print(x)