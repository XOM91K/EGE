import ipaddress
for x in ipaddress.ip_network('22.31.9.215/255.255.254.0', 0):
    print(x)