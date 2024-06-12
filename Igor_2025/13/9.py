import ipaddress
ct = 0
for i in ipaddress.ip_network('172.16.128.0/255.255.192.0', False):
    i = f'{i:b}'
    if i.count('1') % 2 != 0:
        ct += 1
print(ct)