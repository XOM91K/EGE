import ipaddress
for x in ipaddress.ip_network('95.112.224.0/255.255.255.128', False):
    x = f'{x:b}'[24:]
    if x == x[::-1]:
        print(x)