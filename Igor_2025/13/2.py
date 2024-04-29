import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.32.160/255.255.255.240', False):
    x = f'{x:b}'
    if x.count('1') % 2 == 0:
        ct += 1
print(ct)