import ipaddress
l = []
for x in ipaddress.ip_network('204.252.0.0/255.255.0.0', False):
    x = f'{x:b}'
    l.append(x.count('1'))
print(l)
