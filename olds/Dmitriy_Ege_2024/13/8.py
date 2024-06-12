import ipaddress
l = []
for x in ipaddress.ip_network('154.63.100.75/154.63.206.129', False):
    x = f'{x:b}'
    print(x)
print(l)
