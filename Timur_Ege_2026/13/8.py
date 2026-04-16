import ipaddress
for x in ipaddress.ip_network('46.29.170.214/255.255.128.0',0):
    print(x)