import ipaddress
for x in ipaddress.ip_network('25.246.187.249/255.255.255.128', 0):
    print(x)