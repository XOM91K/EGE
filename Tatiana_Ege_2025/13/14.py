import ipaddress
for i in ipaddress.ip_network('210.189.23.15/255.255.248.0', 0):
    print(i)