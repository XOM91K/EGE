import ipaddress
for x in ipaddress.ip_network('192.168.32.160/255.255.255.240', strict=False):
    x = f'{x:b}'
    if x.count('0') > 21:
        print(x)