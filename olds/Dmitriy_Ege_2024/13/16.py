import ipaddress
ct=  0
for x in ipaddress.ip_network('203.111.195.0/255.255.240.0', False):
    x = f'{x:b}'
    if x.count('0') % 3 == 0 and '111' in x and '000' in x:
        ct += 1
print(ct)