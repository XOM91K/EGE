import ipaddress
ct = 0
for x in ipaddress.ip_network('202.75.38.152/255.255.255.248', False):
    x = f'{x:b}'
    if '111' in x:
        print(x)
        ct += 1
print(ct)