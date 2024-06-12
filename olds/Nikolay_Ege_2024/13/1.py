import ipaddress
ct = 0
for x in ipaddress.ip_network('99.64.0.0/255.192.0.0', False):
    x = f'{x:b}'
    if x[-1] == '0':
        ct += 1
print(ct)