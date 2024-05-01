import ipaddress
ct = 0
for x in ipaddress.ip_network('211.48.136.64/255.255.255.224', False):
    x = f'{x:b}'
    if x[-2:] == '11':
        ct += 1
print(ct)