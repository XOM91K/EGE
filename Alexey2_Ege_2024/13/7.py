import ipaddress
ct = 0
for x in ipaddress.ip_network('142.68.56.0/255.255.255.240', strict=False):
    x = f'{x:b}'
    if x[:16].count('1') < x[16:].count('1'):
        print(x)