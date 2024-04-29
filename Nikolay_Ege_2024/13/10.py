import ipaddress
a = []
for x in ipaddress.ip_network('94.159.76.0/255.255.255.128', False):
    x = f'{x:b}'
    print(x.count('0'))
    a.append(x.count('0'))
print(min(a))