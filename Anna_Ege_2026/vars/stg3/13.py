import ipaddress
for x in ipaddress.ip_network('17.234.25.1/255.255.224.0', 0):
    print(x)