import ipaddress
ct = 0
for x in ipaddress.ip_network('106.184.0.0/255.248.0.0', False):
    x = f'{x:b}'
    if x.count('1') % 2 != 0:
        ct += 1
print(ct)