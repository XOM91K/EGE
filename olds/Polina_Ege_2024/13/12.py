import ipaddress
ct = 0
for x in ipaddress.ip_network('154.233.0.0/255.255.0.0', False):
    x = f'{x:b}'
    if x[-1] == '0':
        ct += 1
print(ct)