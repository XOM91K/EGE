import ipaddress
for x in ipaddress.ip_network('95.24.16.0/255.255.240.0',0):
    print(x)