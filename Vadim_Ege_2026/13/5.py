import ipaddress
for x in ipaddress.ip_network('172.45.12.200/255.255.240.0', 0):
    print(x)