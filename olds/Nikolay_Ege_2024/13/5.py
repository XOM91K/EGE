import ipaddress
for x in ipaddress.ip_network('136.36.240.16/255.255.255.248', False):
    x = f'{x:b}'
    if '101' not in x:
        print(x)