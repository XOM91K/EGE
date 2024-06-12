import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.32.48/255.255.255.240', strict=False):
    x = f'{x:b}'
    if x.count('1') % 2 != 0:
        ct += 1
print(ct)

