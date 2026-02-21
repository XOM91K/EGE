import ipaddress
for x in ipaddress.ip_network('190.202.83.62/255.255.252.0', 0):
    print(x)