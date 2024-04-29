import ipaddress
for x in ipaddress.ip_network('202.75.38.152/255.255.255.248'):
    if '111' in f'{x:b}':
        print(f'{x:b}')
