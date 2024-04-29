import ipaddress
ct = 0
for x in ipaddress.ip_network('212.192.32.96/255.255.255.224', False):
    x = f'{x:b}'
    if '000' not in x[-8:] and '111' not in x[-8:]:
        ct += 1
print(ct)