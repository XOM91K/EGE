import ipaddress
for x in ipaddress.ip_network('143.168.72.213/255.255.255.240', 0):
    print(x)