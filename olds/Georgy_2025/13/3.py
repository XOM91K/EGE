import ipaddress
ct = 0
for x in ipaddress.ip_network('69.121.128.142/255.255.252.0', False):
    print(x)