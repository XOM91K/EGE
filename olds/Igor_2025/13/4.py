import ipaddress
ct = 0
for x in ipaddress.ip_network('213.0.0.0/255.192.0.0', False):
    x = f'{x:b}'
    if '111' in x:
        ct += 1
print(ct)