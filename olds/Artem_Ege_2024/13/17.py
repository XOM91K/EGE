import ipaddress
ct = 0
for x in ipaddress.ip_network('122.159.68.144/255.255.255.240', False):
    x = f'{x:b}'
    if x.count('0') % 3 != 0:
        ct += 1
print(ct)