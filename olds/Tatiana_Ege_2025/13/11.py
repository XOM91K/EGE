import ipaddress
for i in ipaddress.ip_network('67.187.123.42/255.255.224.0', 0):
    print(i)