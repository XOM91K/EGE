import ipaddress
for x in ipaddress.ip_network("94.159.76.0/255.255.255.128"):
    x = f'{x:b}'
    print(x.count('0'))