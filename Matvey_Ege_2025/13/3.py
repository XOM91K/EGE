import ipaddress
for i in ipaddress.ip_network('69.121.128.142/255.255.252.0', False):
    print(i)