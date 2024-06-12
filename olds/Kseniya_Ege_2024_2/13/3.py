import ipaddress
ct = 0
for x in ipaddress.ip_network('202.75.38.176/255.255.255.240', False):
    x = f'{x:b}'
    if '111' not in x and '000' not in x:
        ct += 1

print(ct)