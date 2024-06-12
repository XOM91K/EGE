import ipaddress
mn = 10 ** 10
for x in ipaddress.ip_network("94.159.76.0/255.255.255.128", False):
    x = f'{x:b}'
    mn = min(mn, x.count('0'))
print(mn)